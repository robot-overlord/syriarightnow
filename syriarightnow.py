import os
import tweetstream
from flask import Flask

reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)
@app.route('/')

def syriarightnow():
    return 'Hello World!'
