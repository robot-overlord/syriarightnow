# -*- coding: utf-8 -*-

import pika
import json
import keys
import time
import filter
import twitter_api
from tweepy import API
from tweepy import OAuthHandler

def on_open(connection):
    connection.channel(on_channel_open)

def on_message(channel, basic_deliver, properties, body):
    try:
        matches = filter.call(body)

        if any(matches):
            print "Match on " + body
            tweet(body)

        channel.basic_ack(basic_deliver.delivery_tag)
        print "Done consuming " + body

    except BaseException, e:
        print("failed in consumer on message, ", str(e))
        time.sleep(5)
        pass

def on_channel_open(channel):
    try:
        print "Recieving messages..."
        channel.basic_consume(on_message, "social_data")

    except BaseException, e:
        print("failed in consumer on channel open, ", str(e))
        time.sleep(5)
        pass

    # # Cancel the consumer and return any pending messages
    # requeued_messages = channel.cancel()
    # print "Requeued %i messages" % requeued_messages

def tweet(text):
    try:
        print "tweeting " + text + "..."
        twitter_api.connection.update_status(status = text)
        print "Done."

    except BaseException, e:
        print("failed in consumer tweet, ", str(e))
        time.sleep(5)
        pass


connection = pika.SelectConnection(on_open_callback=on_open)

try:
    # Step #2 - Block on the IOLoop
    connection.ioloop.start()

# Catch a Keyboard Interrupt to make sure that the connection is closed cleanly
except KeyboardInterrupt:
    # Gracefully close the connection
    connection.close()
    # Start the IOLoop again so Pika can communicate, it will stop on its own when the connection is closed
    connection.ioloop.start()
