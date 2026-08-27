from __future__ import annotations

import os
import re

import requests

from ipsw_diff_social.models import CatalogEntry, DataError, DiffFact, ReleaseNames

CATALOG_COMMITS_URL = "https://api.github.com/repos/ipsw-diffs/catalog/commits"
CATALOG_RAW_URL = "https://raw.githubusercontent.com/ipsw-diffs/catalog/{commit}/catalog.json"
RELEASES_URL = "https://raw.githubusercontent.com/ipsw-diffs/catalog/main/metadata/releases.json"
REQUEST_TIMEOUT = (10, 30)

_COUNT_HEADING = re.compile(r"^#{3,6}\s+(.+?)\s+\(([\d,]+)\)\s*$")
_PLAIN_HEADING = re.compile(r"^(#{2,5})\s+(.+?)\s*$")
_FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
_FULL_OID = re.compile(r"[0-9a-f]{40}")
_CHANGE_WORDS = {
    "updated": "updated",
    "new": "added",
    "removed": "removed",
}


def fetch_json(session: requests.Session, url: str) -> object:
    response = session.get(url, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.json()


def fetch_text(session: requests.Session, url: str) -> str:
    response = session.get(url, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.text


def fetch_catalog_commit(session: requests.Session) -> str:
    """Resolve the immutable catalog revision currently published on main."""
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    response = session.get(
        CATALOG_COMMITS_URL,
        headers=headers,
        params={"path": "catalog.json", "per_page": 1},
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    value = response.json()
    if not isinstance(value, list) or not value or not isinstance(value[0], dict):
        raise DataError("catalog commit response did not contain a commit")
    commit = value[0].get("sha")
    if not isinstance(commit, str) or _FULL_OID.fullmatch(commit) is None:
        raise DataError("catalog commit response did not contain a full lowercase SHA")
    return commit


def fetch_catalog(session: requests.Session, commit: str) -> list[CatalogEntry]:
    """Fetch and validate the catalog at one immutable Git revision."""
    if _FULL_OID.fullmatch(commit) is None:
        raise DataError("catalog commit must be a full lowercase SHA")
    value = fetch_json(session, CATALOG_RAW_URL.format(commit=commit))
    if not isinstance(value, dict):
        raise DataError("catalog document must be an object")
    rows = value.get("entries")
    if not isinstance(rows, list):
        raise DataError("catalog entries must be an array")
    entries = [CatalogEntry.from_value(row) for row in rows]
    if len({entry.entry_id for entry in entries}) != len(entries):
        raise DataError("catalog contains duplicate entry IDs")
    return entries


def fetch_release_names(session: requests.Session) -> ReleaseNames:
    return ReleaseNames.from_document(fetch_json(session, RELEASES_URL))


def _clean_heading(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9 .&+/-]", "", value).strip()
    return re.sub(r"\s+", " ", cleaned)


def _heading_change(value: str) -> str | None:
    lowered = value.casefold()
    return next(
        (
            normalized
            for word, normalized in _CHANGE_WORDS.items()
            if re.search(rf"\b{re.escape(word)}\b", lowered)
        ),
        None,
    )


def parse_diff_facts(markdown: str, limit: int = 3) -> list[DiffFact]:
    """Extract the largest counted changes from generated diff headings."""
    hierarchy: dict[int, str] = {}
    facts: list[DiffFact] = []
    fence: str | None = None

    for line in markdown.splitlines():
        fence_match = _FENCE.match(line)
        if fence_match is not None:
            marker = fence_match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence is not None:
            continue

        counted = _COUNT_HEADING.match(line)
        if counted is not None:
            heading = _clean_heading(counted.group(1))
            depth = len(line) - len(line.lstrip("#"))
            ancestors = [
                hierarchy[parent_depth]
                for parent_depth in range(depth - 1, 1, -1)
                if parent_depth in hierarchy
            ]
            heading_change = _heading_change(heading)
            ancestor_change = next(
                (change for ancestor in ancestors if (change := _heading_change(ancestor))),
                None,
            )
            change = heading_change or ancestor_change or "changed"
            area = (
                next(
                    (ancestor for ancestor in ancestors if _heading_change(ancestor) is None),
                    "Diff",
                )
                if heading_change is not None
                else heading
            )
            count = int(counted.group(2).replace(",", ""))
            facts.append(DiffFact(area=area, change=change, count=count))
            continue

        plain = _PLAIN_HEADING.match(line)
        if plain is None:
            continue
        depth = len(plain.group(1))
        heading = _clean_heading(plain.group(2))
        if heading:
            hierarchy[depth] = heading
            for deeper in tuple(key for key in hierarchy if key > depth):
                del hierarchy[deeper]

    ordered = sorted(enumerate(facts), key=lambda item: (-item[1].count, item[0]))
    return [fact for _, fact in ordered[:limit]]
