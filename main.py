from spotify import fetch_playlist_tracks
from youtube import download_videos, resolve_video_ids


def run(playlist_url: str | None = None) -> None:
    playlist_url = playlist_url or input("Insert Playlist Link: ").strip()
    tracks = fetch_playlist_tracks(playlist_url)
    video_ids = resolve_video_ids(tracks)
    if not video_ids:
        print("No matching videos found.")
        return
    download_videos(video_ids)


if __name__ == "__main__":
    run()
