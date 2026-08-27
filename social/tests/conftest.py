from __future__ import annotations

from ipsw_diff_social.models import CatalogEntry


def entry_document() -> dict[str, object]:
    return {
        "id": "ios-27.0-24A5418b-24A5424a",
        "platform": "iOS",
        "device": "iPhone18,1",
        "from": {"version": "27.0", "build": "24A5418b"},
        "to": {"version": "27.0", "build": "24A5424a"},
        "destination": {
            "repository": "https://github.com/ipsw-diff/ios-27",
            "commit": "a" * 40,
            "entrypoint": "diffs/example/README.md",
        },
    }


def sample_entry() -> CatalogEntry:
    return CatalogEntry.from_value(entry_document())
