from __future__ import annotations

import argparse
from pathlib import Path

from ipsw_diff_social.publisher import RunConfig, run


def _default_base_image() -> Path:
    return Path(__file__).resolve().parent / "assets" / "ipsw-diff-social-base.png"


def parser() -> argparse.ArgumentParser:
    command = argparse.ArgumentParser(description="Publish new ipsw-diff catalog entries.")
    command.add_argument(
        "--mode",
        choices=("schedule", "bootstrap", "dry-run"),
        default="dry-run",
        help="dry-run renders only; bootstrap suppresses all current entries",
    )
    command.add_argument("--base-image", type=Path, default=_default_base_image())
    command.add_argument("--output-dir", type=Path, default=Path("social-output"))
    command.add_argument(
        "--entry-id",
        help="immutable catalog ID to render in dry-run mode",
    )
    return command


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    return run(
        RunConfig(
            mode=args.mode,
            base_image=args.base_image,
            output_dir=args.output_dir,
            entry_id=args.entry_id or None,
        )
    )
