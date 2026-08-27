from __future__ import annotations

import base64
from pathlib import Path
from types import SimpleNamespace

from conftest import sample_entry
from pytest import MonkeyPatch

from ipsw_diff_social import ai
from ipsw_diff_social.ai import (
    IMAGE_SIZE,
    MAX_RETRIES,
    MODEL,
    REQUEST_TIMEOUT_SECONDS,
    generate_ai_base,
)
from ipsw_diff_social.models import DiffFact


class FakeImages:
    def __init__(self) -> None:
        self.arguments: dict[str, object] = {}

    def edit(self, **kwargs: object) -> object:
        self.arguments = kwargs
        encoded = base64.b64encode(b"fake-png").decode("ascii")
        return SimpleNamespace(data=[SimpleNamespace(b64_json=encoded)])


def test_generate_ai_base_uses_pinned_model_and_writes_result(tmp_path: Path) -> None:
    source = tmp_path / "source.png"
    output = tmp_path / "output.png"
    source.write_bytes(b"source")
    images = FakeImages()
    client = SimpleNamespace(images=images)

    generate_ai_base(
        source,
        output,
        sample_entry(),
        [DiffFact(area="Mach-O", change="updated", count=97)],
        client=client,
    )

    assert output.read_bytes() == b"fake-png"
    assert images.arguments["model"] == MODEL
    assert images.arguments["size"] == IMAGE_SIZE == "1536x864"
    assert "Do not add, alter, or invent any text" in str(images.arguments["prompt"])


def test_generate_ai_base_bounds_default_client_timeout_and_retries(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    source = tmp_path / "source.png"
    output = tmp_path / "output.png"
    source.write_bytes(b"source")
    images = FakeImages()
    arguments: dict[str, object] = {}

    def client_factory(**kwargs: object) -> object:
        arguments.update(kwargs)
        return SimpleNamespace(images=images)

    monkeypatch.setattr(ai, "OpenAI", client_factory)
    generate_ai_base(source, output, sample_entry(), [])

    assert arguments == {"timeout": REQUEST_TIMEOUT_SECONDS, "max_retries": MAX_RETRIES}
