# -*- coding: utf8 -*-
import tweepy
import json
import requests
# http://proinlab.com/archives/1562

f_d = open('disaster.txt').readline()
f_a = open('accident.txt').readline()
f_c = open('crime.txt').readline()

f_output = open('event.txt', 'a')

event_set = [t.strip().replace('_',' ').lower() for t in f_d.split(',')] \
						+ [t.strip().replace('_',' ').lower() for t in f_a.split(',')] \
						+  [t.strip().replace('_',' ').lower() for t in f_c.split(',')]
#print [t.strip().replace('_',' ') for t in f_d.split(',')] 
#print [t.strip().replace('_',' ') for t in f_a.split(',')] 
#print [t.strip().replace('_',' ') for t in f_c.split(',')]
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
			if ('RT' not in js['text']) and (hasNumbers(js['text']) or hasTime(js['text']) and hasHash(js['text'])): 
				for w in js["text"].split(" "):
					if w in event_set:
						#print "%s ############### %s" %(w, js["text"])
						try:
							if js["place"]:
								a =  requests.post('http://localhost/analyzer/store', data = {'tmp' : json.dumps(js) })
								f_output.write(json.dumps(js))
								f_output.write("\n")
								print json.dumps(js)
								if res.status_code == 200:
									print 'saved ---------------------------------------------------'
									print 'saved ---------------------------------------------------'
									print 'saved ---------------------------------------------------'
						except:
							pass
				#print js
		except:
			pass

		return True
	def on_error(self, status):
		print('error : ', status)

twitterStream = tweepy.Stream(auth, listener())
#lang ko
#twitterStream.filter(track=['earthquake', 'tornado', 'car accidents', 'terror'], locations=[125.079346, 32.892849, 129.276123, 38.646372])

# "country_code":"US"
twitterStream.filter(filter_level="low", track=event_set, locations=[-125.112305, 24.584593, -66.665039 , 49.136800])

