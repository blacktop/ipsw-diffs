from __future__ import annotations

import re
from dataclasses import dataclass
from urllib.parse import urlparse

LEGACY_CATALOG_ORG = "ipsw-diff"
PUBLISHING_ORG = "ipsw-diffs"


class DataError(ValueError):
    """Raised when an upstream document does not match the expected schema."""


def _mapping(value: object, field: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise DataError(f"{field} must be an object")
    if not all(isinstance(key, str) for key in value):
        raise DataError(f"{field} keys must be strings")
    return value


def _text(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise DataError(f"{field} must be a non-empty string")
    return value.strip()


@dataclass(frozen=True)
class Release:
    version: str
    build: str

    @classmethod
    def from_value(cls, value: object, field: str) -> Release:
        data = _mapping(value, field)
        return cls(
            version=_text(data.get("version"), f"{field}.version"),
            build=_text(data.get("build"), f"{field}.build"),
        )


@dataclass(frozen=True)
class Destination:
    repository: str
    commit: str
    entrypoint: str

    @classmethod
    def from_value(cls, value: object) -> Destination:
        data = _mapping(value, "destination")
        repository = _text(data.get("repository"), "destination.repository").rstrip("/")
        parsed = urlparse(repository)
        if parsed.scheme != "https" or parsed.netloc != "github.com":
            raise DataError("destination.repository must be an https://github.com URL")
        parts = [part for part in parsed.path.split("/") if part]
        if len(parts) != 2:
            raise DataError("destination.repository must name one GitHub repository")
        if parts[0] not in {LEGACY_CATALOG_ORG, PUBLISHING_ORG}:
            raise DataError("destination.repository must belong to the ipsw-diffs organization")
        # Catalog v1 rows retain the former singular organization after the GitHub rename.
        repository = f"https://github.com/{PUBLISHING_ORG}/{parts[1]}"

        commit = _text(data.get("commit"), "destination.commit")
        if re.fullmatch(r"[0-9a-f]{40}", commit) is None:
            raise DataError("destination.commit must be a full lowercase Git SHA")

        entrypoint = _text(data.get("entrypoint"), "destination.entrypoint")
        if entrypoint.startswith("/") or ".." in entrypoint.split("/"):
            raise DataError("destination.entrypoint must be a safe relative path")
        return cls(repository=repository, commit=commit, entrypoint=entrypoint)

    @property
    def slug(self) -> str:
        return self.repository.removeprefix("https://github.com/")

    @property
    def page_url(self) -> str:
        return f"{self.repository}/blob/{self.commit}/{self.entrypoint}"

    @property
    def raw_url(self) -> str:
        return f"https://raw.githubusercontent.com/{self.slug}/{self.commit}/{self.entrypoint}"


@dataclass(frozen=True)
class CatalogEntry:
    entry_id: str
    platform: str
    device: str
    previous: Release
    current: Release
    destination: Destination

    @classmethod
    def from_value(cls, value: object) -> CatalogEntry:
        data = _mapping(value, "entry")
        entry_id = _text(data.get("id"), "entry.id")
        if re.fullmatch(r"[A-Za-z0-9.,_-]+", entry_id) is None:
            raise DataError("entry.id contains unsupported characters")
        return cls(
            entry_id=entry_id,
            platform=_text(data.get("platform"), "entry.platform"),
            device=_text(data.get("device"), "entry.device"),
            previous=Release.from_value(data.get("from"), "entry.from"),
            current=Release.from_value(data.get("to"), "entry.to"),
            destination=Destination.from_value(data.get("destination")),
        )


@dataclass(frozen=True)
class DiffFact:
    area: str
    change: str
    count: int

    @property
    def summary(self) -> str:
        noun = "item" if self.count == 1 else "items"
        return f"{self.area}: {self.count:,} {noun} {self.change}"


@dataclass(frozen=True)
class ReleaseNames:
    names: dict[tuple[str, str], str]

    @classmethod
    def from_document(cls, value: object) -> ReleaseNames:
        document = _mapping(value, "releases document")
        rows = document.get("releases")
        if not isinstance(rows, list):
            raise DataError("releases must be an array")
        names: dict[tuple[str, str], str] = {}
        for index, row in enumerate(rows):
            data = _mapping(row, f"releases[{index}]")
            platform = _text(data.get("platform"), f"releases[{index}].platform")
            build = _text(data.get("build"), f"releases[{index}].build")
            display = _text(data.get("display_version"), f"releases[{index}].display_version")
            names[(platform, build)] = display
        return cls(names=names)

    def label(self, platform: str, release: Release) -> str:
        return self.names.get((platform, release.build), release.version)
