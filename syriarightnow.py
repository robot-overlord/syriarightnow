import os
from flask import Flask
from rq import Queue
from worker import conn
import tweetstream

q = Queue(connection=conn)
result = q.enqueue(tweetstream.call())

app = Flask(__name__)
@app.route('/')

def syriarightnow():
    return 'Hello World!'
