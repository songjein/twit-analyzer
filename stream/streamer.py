# -*- coding: utf8 -*-
import tweepy
import json
import requests
# http://proinlab.com/archives/1562

f_d = open('disaster.txt').readline()
f_a = open('accident.txt').readline()
f_c = open('crime.txt').readline()

"""
event_set = [t.strip().replace('_',' ').lower() for t in f_d.split(',')] \
						+ [t.strip().replace('_',' ').lower() for t in f_a.split(',')] \
						+  [t.strip().replace('_',' ').lower() for t in f_c.split(',')]
"""
event_set = [t.strip().replace('_',' ').lower() for t in f_d.split(',')]

print event_set

consumer_key='0tIjL8LkOmKNjYTGRU13zVrAJ'
consumer_secret='FdnDaJxTCc46p4RVhaaQab8bfau0VxDiSAjIVVh5f4SXmMsLjn'
access_token='244321827-BVk2am7iaUSSuJzJEENs94DjOTxcu1hpOmUwcjNN'
access_token_secret='7ZXX67Xz9bgfxJqJou6OCiw7mBTuQy2AmU7SslZjgv6XN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

import re
def hasNumbers(s):
	return bool(re.search(r'\d', s)) 

def hasTime(s):
	return bool("AM" in s or "PM" in s or "am" in s or "pm" in s)

def hasHash(s):
	return bool("#" in s) 

def hasURL(s):
	return bool("http" in s) 

class listener(tweepy.streaming.StreamListener):
	def on_data(self, data):
		try:
		# only korea
		#data = data.encode('utf-8')
		#data = data.decode('unicode_escape')
			js = json.loads(data)
			#print js["place"]["country_code"]
			#print js["text"], js["created_at"]
			if js["place"] and js["place"]["country_code"] == "US":
				if (hasNumbers(js['text']) or hasTime(js['text']) or hasHash(js['text'])): 
					print json.dumps(js)
				#res =  requests.post('http://localhost/analyzer/store', data = {'tmp' : json.dumps(js) })
			#print js["place"]["country_code"] == "US"
		except:
			pass

		return True
	def on_error(self, status):
		print('error : ', status)

twitterStream = tweepy.Stream(auth, listener())
#lang ko
#twitterStream.filter(track=['earthquake', 'tornado', 'car accidents', 'terror'], locations=[125.079346, 32.892849, 129.276123, 38.646372])

# "country_code":"US"
#twitterStream.filter(filter_level="low", track=event_set, locations=[-125.112305, 24.584593, -66.665039 , 49.136800])
twitterStream.filter(track=['earthquake', 'tornado', 'car accident'],locations=[-125.112305, 24.584593, -66.665039 , 49.136800])

