from __future__ import annotations

import os
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

import requests

from ipsw_diff_social.ai import generate_ai_base
from ipsw_diff_social.catalog import (
    fetch_catalog,
    fetch_catalog_commit,
    fetch_release_names,
    fetch_text,
    parse_diff_facts,
)
from ipsw_diff_social.models import CatalogEntry, DataError, DiffFact, ReleaseNames
from ipsw_diff_social.render import release_title, render_card
from ipsw_diff_social.state import GitHubIssueStore, PublisherState
from ipsw_diff_social.x_client import XClient, XCredentials

MAX_POSTS_PER_RUN = 3
MAX_POST_WEIGHT = 280
TRANSFORMED_URL_LENGTH = 23
_URL = re.compile(r"https?://\S+")
_SINGLE_WEIGHT_RANGES = ((0, 4351), (8192, 8205), (8208, 8223), (8242, 8247))


@dataclass(frozen=True)
class RunConfig:
    mode: str
    base_image: Path
    output_dir: Path
    entry_id: str | None = None


def _character_weight(character: str) -> int:
    codepoint = ord(character)
    return 1 if any(start <= codepoint <= end for start, end in _SINGLE_WEIGHT_RANGES) else 2


def x_weighted_length(text: str) -> int:
    """Count generated post text using X's weighted-text and t.co URL rules."""
    normalized = unicodedata.normalize("NFC", text)
    weight = 0
    offset = 0
    for match in _URL.finditer(normalized):
        weight += sum(
            _character_weight(character) for character in normalized[offset : match.start()]
        )
        weight += TRANSFORMED_URL_LENGTH
        offset = match.end()
    return weight + sum(_character_weight(character) for character in normalized[offset:])


def _truncate_weighted(text: str, limit: int) -> str:
    result: list[str] = []
    weight = 0
    for character in unicodedata.normalize("NFC", text):
        character_weight = _character_weight(character)
        if weight + character_weight > limit:
            break
        result.append(character)
        weight += character_weight
    return "".join(result).rstrip()


def compose_post(entry: CatalogEntry, names: ReleaseNames, facts: list[DiffFact]) -> str:
    """Compose the richest post that fits X's weighted 280-character limit."""
    header = f"New ipsw-diff: {release_title(entry, names)}"
    lines = [f"• {fact.summary}" for fact in facts]
    url = entry.destination.page_url
    while True:
        body = "\n".join(lines)
        text = f"{header}\n\n{body}\n\n{url}" if body else f"{header}\n\n{url}"
        if x_weighted_length(text) <= MAX_POST_WEIGHT:
            return text
        if lines:
            lines.pop()
            continue
        suffix = f"\n\n{url}"
        available = max(0, MAX_POST_WEIGHT - x_weighted_length(suffix))
        return f"{_truncate_weighted(header, available)}{suffix}"


def _render_entry(
    session: requests.Session,
    config: RunConfig,
    entry: CatalogEntry,
    names: ReleaseNames,
) -> tuple[Path, list[DiffFact]]:
    markdown = fetch_text(session, entry.destination.raw_url)
    facts = parse_diff_facts(markdown)
    base = config.base_image
    ai_output = config.output_dir / f"{entry.entry_id}-ai.png"
    if os.environ.get("OPENAI_API_KEY"):
        try:
            generate_ai_base(base, ai_output, entry, facts)
            base = ai_output
        except Exception as error:  # The deterministic branded fallback must always remain usable.
            detail = " ".join(str(error).split()) or "no error detail"
            print(
                f"AI image generation failed for {entry.entry_id} "
                f"({type(error).__name__}: {detail[:500]}); using branded fallback."
            )

    output = config.output_dir / f"{entry.entry_id}.png"
    render_card(base, output, entry, names, facts)
    return output, facts


def _state_store() -> GitHubIssueStore:
    repository = os.environ.get("GITHUB_REPOSITORY", "")
    token = os.environ.get("GITHUB_TOKEN", "")
    return GitHubIssueStore(repository=repository, token=token)


def run(config: RunConfig) -> int:
    if config.mode not in {"schedule", "bootstrap", "dry-run"}:
        raise ValueError(f"unsupported mode: {config.mode}")
    if not config.base_image.is_file():
        raise FileNotFoundError(f"base image does not exist: {config.base_image}")

    session = requests.Session()
    current_commit = fetch_catalog_commit(session)
    config.output_dir.mkdir(parents=True, exist_ok=True)

    if config.mode == "dry-run":
        entries = fetch_catalog(session, current_commit)
        if not entries:
            print("Catalog is empty; no dry-run card was created.")
            return 0
        if config.entry_id is None:
            raise ValueError(
                "dry-run requires --entry-id because catalog order is not chronological"
            )
        entry = next((item for item in entries if item.entry_id == config.entry_id), None)
        if entry is None:
            raise ValueError(f"catalog entry not found: {config.entry_id}")
        names = fetch_release_names(session)
        image_path, facts = _render_entry(session, config, entry, names)
        print(compose_post(entry, names, facts))
        print(f"Rendered preview: {image_path}")
        return 0

    store = _state_store()
    issue = store.find()
    if issue is None:
        created = store.create(PublisherState(catalog_commit=current_commit))
        print(f"Bootstrapped catalog revision {current_commit} in state issue #{created.number}.")
        return 0

    if config.mode == "bootstrap":
        issue.state.catalog_commit = current_commit
        issue.state.queue.clear()
        issue.state.pending.clear()
        store.save(issue.number, issue.state)
        print(f"Bootstrapped catalog revision {current_commit} in state issue #{issue.number}.")
        return 0

    entries: list[CatalogEntry] | None = None
    if issue.state.catalog_commit != current_commit:
        previous_entries = fetch_catalog(session, issue.state.catalog_commit)
        entries = fetch_catalog(session, current_commit)
        previous_ids = {entry.entry_id for entry in previous_entries}
        current_ids = {entry.entry_id for entry in entries}
        removed = previous_ids - current_ids
        if removed:
            raise DataError(f"catalog removed immutable entry IDs: {sorted(removed)}")
        issue.state.enqueue(current_ids - previous_ids)
        issue.state.catalog_commit = current_commit
        store.save(issue.number, issue.state)

    if not issue.state.queue:
        print("No new catalog entries to publish.")
        if issue.state.pending:
            print(
                f"Fail-closed: {len(issue.state.pending)} pending entr"
                "y/ies require state-issue review before retry."
            )
        return 0

    if entries is None:
        entries = fetch_catalog(session, current_commit)
    entries_by_id = {entry.entry_id: entry for entry in entries}
    missing = issue.state.queue - entries_by_id.keys()
    if missing:
        raise DataError(f"publisher queue references missing catalog entries: {sorted(missing)}")
    candidates = [entries_by_id[entry_id] for entry_id in sorted(issue.state.queue)][
        :MAX_POSTS_PER_RUN
    ]
    if not candidates:
        print("No new catalog entries to publish.")
        return 0

    names = fetch_release_names(session)
    x_client = XClient(XCredentials.from_environment())
    for entry in candidates:
        issue.state.mark_pending(entry.entry_id)
        store.save(issue.number, issue.state)
        try:
            image_path, facts = _render_entry(session, config, entry, names)
            text = compose_post(entry, names, facts)
        except Exception as error:
            detail = " ".join(str(error).split()) or "no error detail"
            print(
                f"Preparation failed for {entry.entry_id} "
                f"({type(error).__name__}: {detail[:500]}); left pending for review."
            )
            continue

        post_id = x_client.publish(text, image_path)
        issue.state.mark_posted(entry.entry_id, post_id)
        store.save(issue.number, issue.state)
        print(f"Published {entry.entry_id} as X post {post_id}.")
    return 0
