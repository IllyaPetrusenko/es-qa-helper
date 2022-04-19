import requests


class Auth:

    def __init__(self, host, credentials):
        self.host = host
        self.credentials = credentials

    def get_tokens(self):
        # get tokens from auth
        tokens = requests.get(url=f'{self.host}auth/signin', headers={
            'Authorization': f'{self.credentials}'
        }).json()

        # access token for the future requests
        access_token = tokens['data']['tokens']['access']
        # token to refresh old access token
        refresh_token = tokens['data']['tokens']['refresh']

        return access_token, refresh_token

    # TODO Add method to refresh old access token
    # def refresh_old_token(self):
