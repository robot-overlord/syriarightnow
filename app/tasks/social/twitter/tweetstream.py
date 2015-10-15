# -*- coding: utf-8 -*-
import os
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import API
from tweepy.streaming import StreamListener
from listener import Listener

ckey = os.environ['TWITTER_CKEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
access_token_key = os.environ['TWITTER_ACCESS_TOKEN_KEY']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

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

def call():
	auth = OAuthHandler(ckey, consumer_secret)
	auth.set_access_token(access_token_key, access_token_secret)

	print("Connecting to Twitter REST API...")
	api = API(auth)
	print("Done.")

	# initialize Stream object
	print("Connecting to Twitter Streaming API...")
	twitterStream = Stream(auth, Listener(api))
	print("Done.")

	# call filter on Stream object
	print("Filter on stream by " + str(user_ids))
	twitterStream.filter(follow=user_ids)
