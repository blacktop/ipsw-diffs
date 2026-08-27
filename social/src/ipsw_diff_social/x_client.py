from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from authlib.integrations.requests_client import OAuth1Session

MEDIA_URL = "https://api.x.com/2/media/upload"
POST_URL = "https://api.x.com/2/tweets"


class _Response(Protocol):
    def raise_for_status(self) -> None: ...

    def json(self) -> object: ...


class _Session(Protocol):
    def post(self, url: str, **kwargs: object) -> _Response: ...


@dataclass(frozen=True)
class XCredentials:
    api_key: str
    api_secret: str
    access_token: str
    access_token_secret: str

    @classmethod
    def from_environment(cls) -> XCredentials:
        names = ("X_API_KEY", "X_API_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET")
        values = {name: os.environ.get(name, "") for name in names}
        missing = [name for name, value in values.items() if not value]
        if missing:
            raise ValueError(f"missing required X credential names: {', '.join(missing)}")
        return cls(
            api_key=values["X_API_KEY"],
            api_secret=values["X_API_SECRET"],
            access_token=values["X_ACCESS_TOKEN"],
            access_token_secret=values["X_ACCESS_TOKEN_SECRET"],
        )


class XClient:
    def __init__(self, credentials: XCredentials, session: _Session | None = None):
        self._session = session or OAuth1Session(
            credentials.api_key,
            credentials.api_secret,
            token=credentials.access_token,
            token_secret=credentials.access_token_secret,
        )

    def upload_image(self, path: Path) -> str:
        with path.open("rb") as image:
            response = self._session.post(
                MEDIA_URL,
                files={"media": (path.name, image, "image/png")},
                data={"media_category": "tweet_image"},
                timeout=(10, 60),
            )
        response.raise_for_status()
        value = response.json()
        if not isinstance(value, dict) or not isinstance(value.get("data"), dict):
            raise RuntimeError("X media response did not contain data")
        data = value["data"]
        media_id = data.get("id") or data.get("media_id")
        if isinstance(media_id, int) and not isinstance(media_id, bool):
            media_id = str(media_id)
        if not isinstance(media_id, str) or not media_id:
            raise RuntimeError("X media response did not contain a media ID")
        return media_id

    def create_post(self, text: str, media_id: str) -> str:
        response = self._session.post(
            POST_URL,
            json={"text": text, "media": {"media_ids": [media_id]}},
            timeout=(10, 30),
        )
        response.raise_for_status()
        value = response.json()
        if not isinstance(value, dict) or not isinstance(value.get("data"), dict):
            raise RuntimeError("X post response did not contain data")
        post_id = value["data"].get("id")
        if not isinstance(post_id, str) or not post_id:
            raise RuntimeError("X post response did not contain a post ID")
        return post_id

    def publish(self, text: str, image_path: Path) -> str:
        return self.create_post(text, self.upload_image(image_path))
