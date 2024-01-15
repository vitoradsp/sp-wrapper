import base64
import requests
import json

class GetToken():
    def __init__(self,
                values:str=None,
                client_id:str=None, 
                client_secret:str=None,
                ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.values = values
    
    def post_get_token(self):
        with open('config.json') as all_data:
            client_data = json.load(all_data)
            self.client_id = client_data['client_id']
            self.client_secret = client_data['client_secret']
        together = self.client_id + ":" + self.client_secret
        encoded_values = together.encode('utf-8')
        encoded_token = str(base64.b64encode(encoded_values), 'utf-8')
        url = 'https://accounts.spotify.com/api/token'
        headers = {
            'content-type':'application/x-www-form-urlencoded',
            'Authorization' : 'Basic ' + encoded_token
                   }
        form = {'grant_type': 'client_credentials'}
        value = requests.post(
            url=url, 
            headers=headers,
            data=form
            ).json()
        self.values = value['access_token']    