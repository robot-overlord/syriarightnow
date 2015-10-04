web: gunicorn syriarightnow:app --log-file=-
worker: python ./tasks/worker.py
tweetstream: python ./tasks/enqueue_tweetstream.py
