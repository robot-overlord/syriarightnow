# -*- coding: utf-8 -*-
import time
import json
import sys
from tweepy.streaming import StreamListener

class Listener(StreamListener):
    def __init__(self, twitter_api, start_time = time.time()):
        self.time = start_time
        self.api = twitter_api

    def on_data(self, data):
        keywords = [
        	u"كيماوي",
        	u"غاز سام",
        	u"كلور",
        	u"اختناق",
        	u"سام",
        	u"غازات سامة",
        	u"الكلور",
        	u"الكيماوي",
        	u"الاختناق",
        	u"الغازات السامة",
        	u"السام"
        ]

        try:
            data = json.loads(data)
            if data["text"]:
                self.filter(data, keywords)
                return True

        except BaseException, e:
            print("failed in ondata, ", str(e))
            time.sleep(5)
            pass

    def on_error(self, status):
        print(status)

    def filter(self, data, keywords):
        print "Incoming tweet from " + data["user"]["screen_name"]
        tweet = data["text"]
        print tweet

        matches = filter(lambda keyword: keyword in tweet, keywords)

        if any(matches):
            print "Match on " + str(matches)
            self.tweet(tweet)
        else:
            print "Do nothing. No keyword match."

        time.sleep(5)

    def tweet(self, text):
        print "tweeting " + text + "..."
        self.api.update_status(status = text)
        print "Done."
