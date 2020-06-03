import sys
import re
import os
import json
import time
import tweepy
import jsonpickle
from pprint import pprint 


#get the following by creating an app on dev.twitter.com
consumer_key = "##"
consumer_secret = "##"
access_token = "##"
access_token_secret = "##"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


maxTweets = 100 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
fName = 'tweetsgeo' # We'll store the tweets in a text file.


place = api.geo_search(query="New York", granularity="city")
place_id = place[0].id


sinceId = None
max_id = -1
tweetCount = 0
print("Downloading max {0} tweetsPerQry".format(maxTweets))


z = os.listdir(os.getcwd())
new_id = str(max(map(int, [re.sub(r'\D', r'', x) for x in [x for x in z if x.startswith('tweetsgeo')]])) + 1)


with open('%s%s.txt' %(fName, new_id), 'w') as f:
    while (1):
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = api.search(q='place:%s' % place_id, count=tweetsPerQry, since='2016-07-15')
                else:
                    new_tweets = api.search(q='place:%s' % place_id, count=tweetsPerQry,
                                            since_id=sinceId, since='2016-07-15')
            else:
                if (not sinceId):
                    new_tweets = api.search(q='place:%s' % place_id, count=tweetsPerQry,
                                            max_id=str(max_id - 1), since='2016-07-15')
                else:
                    new_tweets = api.search(q='place:%s' % place_id, count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId, since='2016-07-15')
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                tweet = tweet._json
                f.write('%s\t%s\t%s\n' %(tweet['id'], tweet['place']['full_name'].encode('utf-8'), ' '.join(tweet['text'].split()).encode('utf-8')))
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error

            print("some error : " + str(e))
            time.sleep(16*60)
 
print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))