import GetOldTweets3 as got
import json

tweetCriteria = got.manager.TweetCriteria().setQuerySearch('europe refugees')\
                                           .setSince("2020-02-16")\
                                           .setUntil("2020-03-01")\
                                           .setMaxTweets(10000000000)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)


j = []
for t in tweet:
    #t.timestamp = t.timestamp.isoformat()
    if "cuomo" in t.text:
        j.append(t.__dict__)
        
file = "cuomo-feb16-29_oldtweets3"
filename = "{}.json".format(file) 

print("Found: {} tweets".format(len(tweet)))

print("Wrote: {} tweets".format(len(j)))

with open(filename, "w") as f:
    f.write(json.dumps(j))