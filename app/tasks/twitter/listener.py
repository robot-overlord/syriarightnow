# -*- coding: utf-8 -*-

import time
import json
import sys
from tasks import filter
from tweepy.streaming import StreamListener

class Listener(StreamListener):
    def __init__(self, twitter_api, start_time = time.time()):
        self.time = start_time
        self.api = twitter_api

    def on_data(self, data):
        try:
            data = json.loads(data)
            if data["text"]:
                self.verify(data)
                return True

        except BaseException, e:
            print("failed in ondata, ", str(e))
            time.sleep(5)
            pass

    def on_error(self, status):
        print(status)

    def verify(self, data):
        print "Incoming tweet from " + data["user"]["screen_name"]
        tweet = data["text"]
        print tweet

        if any(filter.call(tweet)):
            self.tweet(tweet)

        time.sleep(5)

    def tweet(self, text):
        print "tweeting " + text + "..."
        self.api.update_status(status = text)
        print "Done."
