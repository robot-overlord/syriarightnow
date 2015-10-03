# Listener Class Override
import time
import json
from tweepy.streaming import StreamListener
import sys

class Listener(StreamListener):
    def __init__(self, twitter_api, start_time=time.time()):
        self.time = start_time
        self.api = twitter_api

    def on_data(self, data):
        # uids we are currently trackin
        user_ids = [
            842062946,
            896881849,
            786673790,
            1003145436,
            1702767096,
            2767456571,
            2844888263,
            19991403,
            2516461339
        ]

        try:
            uid = json.loads(data)["user"]["id"]
            print "UID:" + str(uid)

            if (uid in user_ids):
                tweet = json.loads(data)["text"] + "something"
                print "tweeting " + tweet + "..."
                self.api.update_status(status = tweet)
                print "Done."
            else:
                print "Do nothing. UID:" + str(uid) + " not tracked."

            time.sleep(5)

            saveFile = open("raw_tweets.json", "a")
            saveFile.write(data)
            saveFile.write("\n")
            saveFile.close()

            return True

        except BaseException, e:
            print "failed in ondata,", str(e)
            time.sleep(5)
            pass

    def on_error(self, status):
        print status
