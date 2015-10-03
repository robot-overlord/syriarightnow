# -*- coding: utf-8 -*-
import os
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import API
from tweepy.streaming import StreamListener
from listener import Listener

ckey = os.environ['CKEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token_key = os.environ['ACCESS_TOKEN_KEY']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

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

def call():
	auth = OAuthHandler(ckey, consumer_secret)
	auth.set_access_token(access_token_key, access_token_secret)

	print "Connecting to Twitter Streaming API..."
	api = API(auth)
	print "Done."

	# initialize Stream object
	twitterStream = Stream(auth, Listener(api))

	# call filter on Stream object
	twitterStream.filter(track=keywords, languages=["ar"])
