from __future__ import annotations

import os
from functools import cache, lru_cache
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

from ipsw_diff_social.models import CatalogEntry, DiffFact, ReleaseNames

CANVAS = (1600, 900)
TEXT_LEFT = 100
TITLE_TOP = 675
MAX_TEXT_WIDTH = 1400


def release_title(entry: CatalogEntry, names: ReleaseNames) -> str:
    before = names.label(entry.platform, entry.previous)
    after = names.label(entry.platform, entry.current)
    return f"{entry.platform} {before} → {entry.platform} {after}"


@lru_cache(maxsize=1)
def _font_path() -> str | None:
    candidates = (
        os.environ.get("SOCIAL_FONT_PATH"),
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    )
    return next(
        (candidate for candidate in candidates if candidate and Path(candidate).is_file()), None
    )


@cache
def _font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    path = _font_path()
    if path is not None:
        return ImageFont.truetype(path, size=size)
    return ImageFont.load_default(size=size)


def _fit_font(
    draw: ImageDraw.ImageDraw, text: str, max_size: int, min_size: int
) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    sizes = list(range(max_size, min_size - 1, -2))
    if not sizes or sizes[-1] != min_size:
        sizes.append(min_size)
    for size in sizes:
        font = _font(size)
        left, _, right, _ = draw.textbbox((0, 0), text, font=font)
        if right - left <= MAX_TEXT_WIDTH:
            return font
    return _font(min_size)


def render_card(
    base_path: Path,
    output_path: Path,
    entry: CatalogEntry,
    names: ReleaseNames,
    facts: list[DiffFact],
) -> None:
    with Image.open(base_path) as source:
        image = ImageOps.fit(source.convert("RGB"), CANVAS, method=Image.Resampling.LANCZOS)

    overlay = Image.new("RGBA", CANVAS, (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.rectangle((0, 625, CANVAS[0], CANVAS[1]), fill=(10, 9, 13, 224))
    image = Image.alpha_composite(image.convert("RGBA"), overlay)
    draw = ImageDraw.Draw(image)

    title = release_title(entry, names)
    title_font = _fit_font(draw, title, max_size=66, min_size=38)
    draw.text((TEXT_LEFT, TITLE_TOP), title, font=title_font, fill=(255, 255, 255, 255))

    build_text = f"{entry.previous.build}  →  {entry.current.build}   •   {entry.device}"
    draw.text((TEXT_LEFT, 760), build_text, font=_font(29), fill=(184, 174, 203, 255))

    if facts:
        fact_text = "   •   ".join(f"{fact.count:,} {fact.area} {fact.change}" for fact in facts)
        fact_font = _fit_font(draw, fact_text, max_size=25, min_size=18)
        draw.text((TEXT_LEFT, 815), fact_text, font=fact_font, fill=(211, 205, 220, 255))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.convert("RGB").save(output_path, format="PNG", optimize=True)
