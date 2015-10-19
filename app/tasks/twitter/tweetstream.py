# -*- coding: utf-8 -*-

import os
from tweepy import Stream
from tweepy.streaming import StreamListener
from listener import Listener

# uids we are currently tracking
user_ids = [
	"842062946",
	"896881849",
	"786673790",
	"1003145436",
	"1702767096",
	"2767456571",
	"2844888263",
	"19991403",
	"2516461339"
]

def call(twitter_api):
	# initialize Stream object
	print("Connecting to Twitter Streaming API...")
	twitterStream = Stream(twitter_api.auth, Listener())
	print("Done.")

	# call filter on Stream object
	print("Filter on stream by " + str(user_ids))
	twitterStream.filter(follow=user_ids)
