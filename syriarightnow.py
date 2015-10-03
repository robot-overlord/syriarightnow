import os
from flask import Flask
import tweetstream

app = Flask(__name__)

def syriarightnow():
    tweetstream.call()
