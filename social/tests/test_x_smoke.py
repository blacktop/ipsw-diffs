from __future__ import annotations

from ipsw_diff_social.x_smoke import smoke_text


def test_smoke_text_identifies_the_unique_workflow_run() -> None:
    assert smoke_text("33038250635") == (
        "ipsw-diff X API smoke test (GitHub Actions run 33038250635) — safe to ignore."
    )
