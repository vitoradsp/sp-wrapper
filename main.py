import re
import tekore as tk
from sideutil import GetToken
from ytmusicapi import YTMusic
import youtube_dl

class Playlist(GetToken):
    def __init__(
        self,
        user_playlist: str=str(
        input("Insert Playlist Link: ")),
        all_items:str=None
        ):
        super().__init__()
        self.user_playlist = user_playlist
        self.all_items = all_items
        self.post_get_token()
        self.get_values_by_playlist_id()


    def get_values_by_playlist_id(self):
        self.user_playlist = re.split(r'[/|?]', self.user_playlist)
        spotify = tk.Spotify(self.values)
        response = spotify.playlist_items(self.user_playlist[4])
        self.all_items = spotify.all_items(response)
        '''url = f'https://api.spotify.com/v1/playlists/{self.user_playlist[4]}/tracks?fields=items(track(name))'
        headers = {'Authorization' : 'Bearer ' + self.values}
        response = requests.get(
            url,
            headers=headers
            ).json()'''

class Get_yt_music(Playlist):
    def __init__(self, urls:list=[]):
        super().__init__()
        self.urls = urls
        self.search_song()

    def search_song(self):
        yt = YTMusic()
        for x in self.all_items:
            search_result = yt.search(
            query=x.track.name,
            limit=1,
            ignore_spelling=False
            )
            for y in search_result:
                if 'title' in y and y['category'] == 'Top result' and 'videoId' in y and 'artists' in y and len(y['artists'])>0 and (artistval == {x.track.artist[0].name} for artistval in y['artists'][0]['name']):
                    self.urls.append(y['videoId'])
                else:
                    pass


class Downloader(Get_yt_music):
    def __init__(self):
        super().__init__()
        self.download_songg()
    
    def download_songg(self):
        ydl_opts = {
            'verbose': True,
            'format':'bestaudio/best',
            'postprocessors':[
            {
                'key':'FFmpegExtractAudio',
                'preferredcodec':'mp3',
                'preferredquality':'192'
                }
            ]
                    }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            for url in self.urls:
                ydl.download([f'https://www.youtube.com/watch?v={url}'])


playlist = Playlist()
get_yt_msc = Get_yt_music()
download_song = Downloader()