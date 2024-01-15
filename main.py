import re
import tekore as tk
from sideutil import GetToken
from ytmusicapi import YTMusic


class Playlist(GetToken):
    def __init__(self, user_playlist: str=str(input("Insert Playlist Link: ")), all_items:str=None):
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
    def __init__(self):
        super().__init__()
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
                print(x.track.artists[0])
                if 'title' in y and y['category'] == 'Top result' and (artistval == f'{x.track.artist}' for artistval in y['artists']):
                    print(f"{y['title']}\n")
                else:
                    pass



    
           


playlist = Playlist()
get_yt_msc = Get_yt_music()