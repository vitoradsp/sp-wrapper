import re
import tekore as tk
from sideutil import GetToken
import ytmusicapi




class Playlist(GetToken):
    def __init__(self, user_playlist: str=str(input("Insert Playlist Link: "))):
        super().__init__()
        self.user_playlist = user_playlist
        self.post_get_token()
        self.get_values_by_playlist_id()

    def get_values_by_playlist_id(self):
        self.user_playlist = re.split(r'[/|?]', self.user_playlist)
        spotify = tk.Spotify(self.values)
        response = spotify.playlist_items(self.user_playlist[4])
        a_items = spotify.all_items(response)
        '''url = f'https://api.spotify.com/v1/playlists/{self.user_playlist[4]}/tracks?fields=items(track(name))'
        headers = {'Authorization' : 'Bearer ' + self.values}
        response = requests.get(
            url,
            headers=headers
            ).json()'''
        a = open(
            'results.txt',
            'w'
            )
        for x in a_items:
            a.write(f"{x.track.name}\n")

        a.close()
           


playlist = Playlist()
