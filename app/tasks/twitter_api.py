import keys
from tweepy import API
from tweepy import OAuthHandler

class TwitterAPI:
    def __init__(self):
        self.auth = OAuthHandler(keys.ckey, keys.consumer_secret)
        self.auth.set_access_token(keys.access_token_key, keys.access_token_secret)
        self.connection = API(self.auth)
