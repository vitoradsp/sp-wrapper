import re

import tekore as tk

from auth import get_spotify_token
from exceptions import SpotifyError

PLAYLIST_URL_EXAMPLE = (
    "https://open.spotify.com/playlist/3Sqos19FbXzYcedJjhs4Qx?si=9eb836fd378a445b"
)
PLAYLIST_ID_PART_INDEX = 4


def parse_playlist_id(url: str) -> str:
    parts = re.split(r"[/|?]", url.strip())
    try:
        return parts[PLAYLIST_ID_PART_INDEX]
    except IndexError as exc:
        raise SpotifyError(
            f"Invalid playlist link. Example: {PLAYLIST_URL_EXAMPLE}"
        ) from exc


def track_artist_name(track) -> str:
    artists = getattr(track, "artists", None) or getattr(track, "artist", None)
    if not artists:
        return ""
    first = artists[0] if isinstance(artists, list) else artists
    return getattr(first, "name", str(first))


def fetch_playlist_tracks(playlist_url: str, token: str | None = None):
    token = token or get_spotify_token()
    playlist_id = parse_playlist_id(playlist_url)
    spotify = tk.Spotify(token)
    response = spotify.playlist_items(playlist_id)
    return spotify.all_items(response)
