# -*- coding: utf8 -*-
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import requests

import numpy as np
# http://proinlab.com/archives/1562

f_d = open('disaster.txt').readline()
f_a = open('accident.txt').readline()
f_c = open('crime.txt').readline()

event_set = [t.strip().replace('_',' ').lower() for t in f_d.split(',')] \
						+ [t.strip().replace('_',' ').lower() for t in f_a.split(',')] \
						+  [t.strip().replace('_',' ').lower() for t in f_c.split(',')]
print event_set

consumer_key='0tIjL8LkOmKNjYTGRU13zVrAJ'
consumer_secret='FdnDaJxTCc46p4RVhaaQab8bfau0VxDiSAjIVVh5f4SXmMsLjn'
access_token='244321827-BVk2am7iaUSSuJzJEENs94DjOTxcu1hpOmUwcjNN'
access_token_secret='7ZXX67Xz9bgfxJqJou6OCiw7mBTuQy2AmU7SslZjgv6XN'

import re
def hasNumbers(s):
	#for num in [int(w) for w in s.split() if w.isdigit()]:
	#	if num < 60:
	#		return True
	#return False
	return bool(re.search(r'\d', s)) 

def hasTimeMark(s):
	return bool("AM" in s or "PM" in s)

def hasHash(s):
	return bool("#" in s) 

def hasURL(s):
	return bool("http" in s) 

def hasKeywords(s):
	cnt = 0 
	for w in event_set:
		if w in s:
			print w
			print w
			print w
			print w
			print w
			print w
			cnt += 1

	if cnt >= 1:
		return True
	return False

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
	def on_data(self, data):
		js = json.loads(data)
		if ('text' in js.keys()) and hasKeywords(js['text']):
			tmp = {}
			tmp["text"] = js["text"]
			tmp["user"] = js["user"]
			tmp["created_at"] = js["created_at"]
			tmp["place"] = js["place"]
			print json.dumps(tmp)
			return True

	def on_error(self, status):
		print status


if __name__ == '__main__':
	#This handles Twitter authetification and the connection to Twitter Streaming API
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)

	#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
	#stream.filter(track=['python', 'javascript', 'ruby'])
	#stream.filter(track=['python', 'javascript', 'ruby'])

	#stream.filter(languages=["en"], track=['earthquake', 'tornado', 'accident' ], locations=[-125.112305, 24.584593, -66.665039 , 49.136800])
	stream.filter(languages=["en"], locations=[-125.112305, 24.584593, -66.665039 , 49.136800])
