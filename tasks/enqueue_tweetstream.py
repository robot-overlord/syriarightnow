# from rq import Queue
# from worker import conn
import tweetstream
#
# q = Queue(connection=conn)
# result = q.enqueue(tweetstream.call())

tweetstream.call()
