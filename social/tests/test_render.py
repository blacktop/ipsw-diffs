from __future__ import annotations

from pathlib import Path

from conftest import sample_entry
from PIL import Image

from ipsw_diff_social.cli import _default_base_image
from ipsw_diff_social.models import DiffFact, ReleaseNames
from ipsw_diff_social.render import CANVAS, release_title, render_card


def names() -> ReleaseNames:
    return ReleaseNames(
        names={
            ("iOS", "24A5418b"): "27.0 beta 6",
            ("iOS", "24A5424a"): "27.0 beta 7",
        }
    )


def test_release_title_uses_release_metadata() -> None:
    assert release_title(sample_entry(), names()) == "iOS 27.0 beta 6 → iOS 27.0 beta 7"


def test_render_card_has_social_dimensions(tmp_path: Path) -> None:
    base = tmp_path / "base.png"
    output = tmp_path / "output.png"
    Image.new("RGB", (1672, 941), "#161419").save(base)

    render_card(
        base,
        output,
        sample_entry(),
        names(),
        [DiffFact(area="Mach-O", change="updated", count=97)],
    )

    with Image.open(output) as rendered:
        assert rendered.size == CANVAS
        assert rendered.format == "PNG"


def test_default_brand_image_is_packaged_with_module() -> None:
    assert _default_base_image().is_file()
