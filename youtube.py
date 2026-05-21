import youtube_dl
from ytmusicapi import YTMusic

from exceptions import YoutubeError
from spotify import track_artist_name

YDL_OPTS = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}


def _is_top_result_match(result: dict, artist_name: str) -> bool:
    if result.get("category") != "Top result":
        return False
    if "videoId" not in result or "title" not in result:
        return False
    artists = result.get("artists") or []
    if not artists:
        return False
    yt_artist = artists[0].get("name", "")
    return yt_artist.lower() == artist_name.lower()


def find_video_id(yt: YTMusic, track_name: str, artist_name: str) -> str | None:
    try:
        results = yt.search(query=track_name, limit=1, ignore_spelling=False)
    except Exception as exc:
        raise YoutubeError(f"YouTube search failed for '{track_name}'.") from exc

    for result in results:
        if _is_top_result_match(result, artist_name):
            return result["videoId"]
    return None


def resolve_video_ids(tracks) -> list[str]:
    yt = YTMusic()
    video_ids: list[str] = []

    for item in tracks:
        track = item.track
        video_id = find_video_id(yt, track.name, track_artist_name(track))
        if video_id:
            video_ids.append(video_id)

    return video_ids


def download_videos(video_ids: list[str], ydl_opts: dict | None = None) -> None:
    opts = ydl_opts or YDL_OPTS
    with youtube_dl.YoutubeDL(opts) as ydl:
        for video_id in video_ids:
            ydl.download([f"https://www.youtube.com/watch?v={video_id}"])
