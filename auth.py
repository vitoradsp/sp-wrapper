import base64
import json
from pathlib import Path

import requests

CONFIG_PATH = Path(__file__).resolve().parent / "config.json"
TOKEN_URL = "https://accounts.spotify.com/api/token"


def load_credentials(path: Path = CONFIG_PATH) -> tuple[str, str]:
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    return data["client_id"], data["client_secret"]


def get_spotify_token(
    client_id: str | None = None,
    client_secret: str | None = None,
    path: Path = CONFIG_PATH,
) -> str:
    if client_id is None or client_secret is None:
        client_id, client_secret = load_credentials(path)

    encoded = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    response = requests.post(
        TOKEN_URL,
        headers={
            "content-type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {encoded}",
        },
        data={"grant_type": "client_credentials"},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["access_token"]
