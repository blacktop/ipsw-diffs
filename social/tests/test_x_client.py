from __future__ import annotations

from pathlib import Path

from ipsw_diff_social.x_client import MEDIA_URL, POST_URL, XClient, XCredentials


class FakeResponse:
    def __init__(self, value: object):
        self.value = value

    def raise_for_status(self) -> None:
        return None

    def json(self) -> object:
        return self.value


class FakeSession:
    def __init__(self, media_id: str | int = "media-1") -> None:
        self.calls: list[tuple[str, dict[str, object]]] = []
        self.media_id = media_id

    def post(self, url: str, **kwargs: object) -> FakeResponse:
        self.calls.append((url, kwargs))
        if url == MEDIA_URL:
            return FakeResponse({"data": {"id": self.media_id}})
        return FakeResponse({"data": {"id": "post-1"}})


def test_publish_uploads_image_then_creates_post(tmp_path: Path) -> None:
    image = tmp_path / "card.png"
    image.write_bytes(b"png")
    session = FakeSession()
    credentials = XCredentials("key", "secret", "token", "token-secret")

    post_id = XClient(credentials, session=session).publish("hello", image)

    assert post_id == "post-1"
    assert [url for url, _ in session.calls] == [MEDIA_URL, POST_URL]
    assert session.calls[1][1]["json"] == {
        "text": "hello",
        "media": {"media_ids": ["media-1"]},
    }


def test_publish_accepts_legacy_numeric_media_id(tmp_path: Path) -> None:
    image = tmp_path / "card.png"
    image.write_bytes(b"png")
    session = FakeSession(media_id=123456789)
    credentials = XCredentials("key", "secret", "token", "token-secret")

    XClient(credentials, session=session).publish("hello", image)

    assert session.calls[1][1]["json"] == {
        "text": "hello",
        "media": {"media_ids": ["123456789"]},
    }


def test_create_post_without_media_sends_text_only() -> None:
    session = FakeSession()
    credentials = XCredentials("key", "secret", "token", "token-secret")

    post_id = XClient(credentials, session=session).create_post("smoke test")

    assert post_id == "post-1"
    assert session.calls == [
        (
            POST_URL,
            {
                "json": {"text": "smoke test"},
                "timeout": (10, 30),
            },
        )
    ]
