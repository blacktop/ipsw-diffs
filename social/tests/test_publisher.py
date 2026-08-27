from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import pytest
from conftest import entry_document, sample_entry
from pytest import MonkeyPatch

from ipsw_diff_social import publisher
from ipsw_diff_social.models import CatalogEntry, DiffFact, ReleaseNames
from ipsw_diff_social.publisher import RunConfig, compose_post, x_weighted_length
from ipsw_diff_social.state import PublisherState, StateIssue

OLD_COMMIT = "1" * 40
CURRENT_COMMIT = "2" * 40


def _entry(entry_id: str) -> CatalogEntry:
    value = entry_document()
    value["id"] = entry_id
    return CatalogEntry.from_value(value)


def _config(tmp_path: Path, mode: str = "schedule", entry_id: str | None = None) -> RunConfig:
    base = tmp_path / "base.png"
    base.write_bytes(b"present")
    return RunConfig(
        mode=mode,
        base_image=base,
        output_dir=tmp_path / "output",
        entry_id=entry_id,
    )


def test_compose_post_includes_exact_title_facts_and_immutable_link() -> None:
    names = ReleaseNames(
        names={
            ("iOS", "24A5418b"): "27.0 beta 6",
            ("iOS", "24A5424a"): "27.0 beta 7",
        }
    )

    text = compose_post(
        sample_entry(),
        names,
        [DiffFact(area="Mach-O", change="updated", count=97)],
    )

    assert "iOS 27.0 beta 6 → iOS 27.0 beta 7" in text
    assert "97 items updated" in text
    assert "/blob/" in text
    assert x_weighted_length(text) <= 280


def test_compose_post_counts_long_urls_as_t_co_links() -> None:
    value = entry_document()
    destination = value["destination"]
    assert isinstance(destination, dict)
    destination["entrypoint"] = f"diffs/{'long-path/' * 12}README.md"
    entry = CatalogEntry.from_value(value)
    facts = [
        DiffFact(area="Mach-O", change="updated", count=97),
        DiffFact(area="filesystem", change="added", count=26),
        DiffFact(area="DSC", change="removed", count=3),
    ]

    text = compose_post(entry, ReleaseNames(names={}), facts)

    assert all(fact.summary in text for fact in facts)
    assert len(text) > 280
    assert x_weighted_length(text) <= 280


def test_compose_post_truncates_an_oversized_header_on_weight_boundary() -> None:
    value = entry_document()
    value["from"] = {"version": "a" * 200, "build": "24A5418b"}
    value["to"] = {"version": "b" * 200, "build": "24A5424a"}
    entry = CatalogEntry.from_value(value)

    text = compose_post(entry, ReleaseNames(names={}), [])

    assert text.endswith(entry.destination.page_url)
    assert x_weighted_length(text) <= 280


def test_compose_post_drops_only_trailing_facts_until_it_fits() -> None:
    facts = [
        DiffFact(area=f"{'a' * 55}-{index}", change="updated", count=index) for index in range(1, 4)
    ]

    text = compose_post(sample_entry(), ReleaseNames(names={}), facts)

    assert facts[0].summary in text
    assert facts[-1].summary not in text
    assert x_weighted_length(text) <= 280


class FakeStore:
    def __init__(self, issue: StateIssue | None = None) -> None:
        self.issue = issue
        self.created: PublisherState | None = None
        self.saved: list[PublisherState] = []

    def find(self) -> StateIssue | None:
        return self.issue

    def create(self, state: PublisherState) -> StateIssue:
        self.created = deepcopy(state)
        return StateIssue(number=7, state=state)

    def save(self, _number: int, state: PublisherState) -> None:
        self.saved.append(deepcopy(state))


def test_first_scheduled_run_bootstraps_without_fetching_or_posting(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    store = FakeStore()
    monkeypatch.setattr(publisher, "fetch_catalog_commit", lambda _session: CURRENT_COMMIT)
    monkeypatch.setattr(
        publisher,
        "fetch_catalog",
        lambda *_args: pytest.fail("initialization must not fetch catalog contents"),
    )
    monkeypatch.setattr(publisher, "_state_store", lambda: store)

    result = publisher.run(_config(tmp_path))

    assert result == 0
    assert store.created == PublisherState(catalog_commit=CURRENT_COMMIT)


def test_schedule_diffs_revisions_and_saves_checkpoint_before_render(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    old_entry = _entry("old")
    new_entry = _entry("new")
    state = PublisherState(catalog_commit=OLD_COMMIT)
    store = FakeStore(StateIssue(number=7, state=state))
    events: list[str] = []

    monkeypatch.setattr(publisher, "fetch_catalog_commit", lambda _session: CURRENT_COMMIT)
    monkeypatch.setattr(
        publisher,
        "fetch_catalog",
        lambda _session, commit: [old_entry] if commit == OLD_COMMIT else [old_entry, new_entry],
    )
    monkeypatch.setattr(publisher, "fetch_release_names", lambda _session: ReleaseNames(names={}))
    monkeypatch.setattr(publisher, "_state_store", lambda: store)
    monkeypatch.setattr(
        publisher,
        "_render_entry",
        lambda *_args: (events.append("render") or tmp_path / "card.png", []),
    )

    class FakeXClient:
        def publish(self, _text: str, _image: Path) -> str:
            events.append("publish")
            return "post-1"

    monkeypatch.setattr(publisher.XCredentials, "from_environment", lambda: object())
    monkeypatch.setattr(publisher, "XClient", lambda _credentials: FakeXClient())

    result = publisher.run(_config(tmp_path))

    assert result == 0
    assert store.saved[0].catalog_commit == CURRENT_COMMIT
    assert store.saved[0].queue == {"new"}
    assert set(store.saved[1].pending) == {"new"}
    assert events == ["render", "publish"]
    assert store.saved[-1].posts == {"new": "post-1"}


def test_preparation_failure_is_quarantined_without_blocking_later_queue_entries(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    first = _entry("a-first")
    second = _entry("b-second")
    state = PublisherState(catalog_commit=CURRENT_COMMIT, queue={first.entry_id, second.entry_id})
    store = FakeStore(StateIssue(number=7, state=state))
    published: list[str] = []

    monkeypatch.setattr(publisher, "fetch_catalog_commit", lambda _session: CURRENT_COMMIT)
    monkeypatch.setattr(publisher, "fetch_catalog", lambda _session, _commit: [first, second])
    monkeypatch.setattr(publisher, "fetch_release_names", lambda _session: ReleaseNames(names={}))
    monkeypatch.setattr(publisher, "_state_store", lambda: store)

    def render(
        _session: object,
        _config: RunConfig,
        entry: CatalogEntry,
        _names: ReleaseNames,
    ) -> tuple[Path, list[DiffFact]]:
        if entry.entry_id == first.entry_id:
            raise OSError("missing immutable README")
        return tmp_path / "card.png", []

    class FakeXClient:
        def publish(self, text: str, _image: Path) -> str:
            published.append(text)
            return "post-2"

    monkeypatch.setattr(publisher, "_render_entry", render)
    monkeypatch.setattr(publisher.XCredentials, "from_environment", lambda: object())
    monkeypatch.setattr(publisher, "XClient", lambda _credentials: FakeXClient())

    result = publisher.run(_config(tmp_path))

    assert result == 0
    assert len(published) == 1
    assert second.destination.page_url in published[0]
    assert first.entry_id in state.pending
    assert second.entry_id in state.posts
    assert not state.queue


def test_x_failure_leaves_persisted_pending_marker_before_request(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    entry = sample_entry()
    state = PublisherState(catalog_commit=CURRENT_COMMIT, queue={entry.entry_id})
    store = FakeStore(StateIssue(number=7, state=state))

    monkeypatch.setattr(publisher, "fetch_catalog_commit", lambda _session: CURRENT_COMMIT)
    monkeypatch.setattr(publisher, "fetch_catalog", lambda _session, _commit: [entry])
    monkeypatch.setattr(publisher, "fetch_release_names", lambda _session: ReleaseNames(names={}))
    monkeypatch.setattr(publisher, "_state_store", lambda: store)
    monkeypatch.setattr(
        publisher,
        "_render_entry",
        lambda *_args: (tmp_path / "card.png", []),
    )

    class FailingXClient:
        def publish(self, _text: str, _image: Path) -> str:
            assert set(store.saved[-1].pending) == {entry.entry_id}
            raise RuntimeError("ambiguous X failure")

    monkeypatch.setattr(publisher.XCredentials, "from_environment", lambda: object())
    monkeypatch.setattr(publisher, "XClient", lambda _credentials: FailingXClient())

    with pytest.raises(RuntimeError, match="ambiguous X failure"):
        publisher.run(_config(tmp_path))

    assert state.queue == set()
    assert set(state.pending) == {entry.entry_id}
    assert state.posts == {}


def test_dry_run_requires_explicit_id_for_nonempty_catalog(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(publisher, "fetch_catalog_commit", lambda _session: CURRENT_COMMIT)
    monkeypatch.setattr(publisher, "fetch_catalog", lambda _session, _commit: [sample_entry()])

    with pytest.raises(ValueError, match="requires --entry-id"):
        publisher.run(_config(tmp_path, mode="dry-run"))


def test_dry_run_empty_catalog_succeeds_without_artifact(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(publisher, "fetch_catalog_commit", lambda _session: CURRENT_COMMIT)
    monkeypatch.setattr(publisher, "fetch_catalog", lambda _session, _commit: [])

    assert publisher.run(_config(tmp_path, mode="dry-run")) == 0
    assert list((tmp_path / "output").iterdir()) == []
