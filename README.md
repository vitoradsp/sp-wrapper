# sp-wrapper

Downloads all tracks from a Spotify playlist as MP3 via YouTube Music search.

## Setup

```bash
pip install -r requirements.txt
```

Add your Spotify API credentials to `config.json`:

```json
{
  "client_id": "your_client_id",
  "client_secret": "your_client_secret"
}
```

Requires [FFmpeg](https://ffmpeg.org/) on your PATH for audio conversion.

## Usage

```bash
python main.py
```

Paste a playlist URL when prompted, for example:

`https://open.spotify.com/playlist/3Sqos19FbXzYcedJjhs4Qx?si=9eb836fd378a445b`

## Project layout

| Module       | Responsibility                          |
| ------------ | --------------------------------------- |
| `auth.py`    | Load credentials and obtain Spotify token |
| `spotify.py` | Parse playlist URL and fetch track list |
| `youtube.py` | Match tracks on YouTube and download MP3 |
| `main.py`    | Run the pipeline end-to-end             |
