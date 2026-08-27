from __future__ import annotations

import base64
from pathlib import Path
from typing import Protocol

from openai import OpenAI

from ipsw_diff_social.models import CatalogEntry, DiffFact

MODEL = "gpt-image-2"
IMAGE_SIZE = "1536x864"
REQUEST_TIMEOUT_SECONDS = 240.0
MAX_RETRIES = 1


class _ImageResult(Protocol):
    b64_json: str | None


class _ImageResponse(Protocol):
    data: list[_ImageResult]


class _ImageEditor(Protocol):
    def edit(self, **kwargs: object) -> _ImageResponse: ...


class _Client(Protocol):
    images: _ImageEditor


def _prompt(entry: CatalogEntry, facts: list[DiffFact]) -> str:
    fact_text = ", ".join(fact.summary for fact in facts) or "an Apple firmware diff"
    return (
        "Edit this supplied ipsw-diff social card into a polished technical release visual. "
        "Preserve the existing file icons, Apple silhouettes, ipsw-diff wordmark, dark palette, "
        "purple accent, and 16:9 composition. Add only subtle abstract data-diff motifs inspired "
        f"by these verified findings: {fact_text}. Platform: {entry.platform}. "
        "Do not add, alter, or invent any text, numbers, logos, watermarks, badges, UI panels, "
        "screenshots, or code. Keep the entire bottom 31 percent dark, quiet, and empty so exact "
        "release text can be overlaid later. Maintain strong contrast and generous negative space."
    )


def generate_ai_base(
    source_path: Path,
    output_path: Path,
    entry: CatalogEntry,
    facts: list[DiffFact],
    client: _Client | None = None,
) -> None:
    api = (
        client
        if client is not None
        else OpenAI(timeout=REQUEST_TIMEOUT_SECONDS, max_retries=MAX_RETRIES)
    )
    with source_path.open("rb") as source:
        response = api.images.edit(
            model=MODEL,
            image=[source],
            prompt=_prompt(entry, facts),
            size=IMAGE_SIZE,
            quality="medium",
            output_format="png",
        )

    if not response.data or not response.data[0].b64_json:
        raise RuntimeError("OpenAI image edit returned no image data")
    try:
        image_bytes = base64.b64decode(response.data[0].b64_json, validate=True)
    except ValueError as error:
        raise RuntimeError("OpenAI image edit returned invalid base64") from error
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(image_bytes)
