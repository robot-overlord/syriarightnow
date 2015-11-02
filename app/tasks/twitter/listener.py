# -*- coding: utf-8 -*-

import time
import json
import sys
import pika
import os
import urlparse
from tweepy.streaming import StreamListener

class Listener(StreamListener):
    def __init__(self):
        #setup rabbitMQ Connection
        url_str = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost//')
        url = urlparse.urlparse(url_str)
        params = pika.ConnectionParameters(host=url.hostname,
                                           virtual_host=url.path[1:],
                                           credentials=pika.PlainCredentials(url.username, url.password))

        connection = pika.BlockingConnection(params)
    	self.channel = connection.channel()

    	#set max queue size
    	args = {"x-max-length": 2000}

    	self.channel.queue_declare(queue='social_data', arguments=args)

    def on_data(self, data):
        try:
            data = json.loads(data)
            if data["text"]:
                self.verify(data)
                time.sleep(5)
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

        # enqueue the tweet
        self.channel.basic_publish(exchange='',
                                   routing_key='social_data',
                                   body=data["text"])
