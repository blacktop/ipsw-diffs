from __future__ import annotations

import os

from ipsw_diff_social.x_client import XClient, XCredentials


def smoke_text(run_id: str) -> str:
    return f"ipsw-diff X API smoke test (GitHub Actions run {run_id}) — safe to ignore."


def main() -> int:
    run_id = os.environ.get("GITHUB_RUN_ID", "unknown")
    post_id = XClient(XCredentials.from_environment()).create_post(smoke_text(run_id))
    print(f"Created X post: https://x.com/i/web/status/{post_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
