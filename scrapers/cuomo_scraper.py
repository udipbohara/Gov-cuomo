# Python program to read 
# json file 
from twitterscraper import query_tweets
import datetime as dt 
import json
import os
import time


query = "(from:NYGovCuomo) until:2020-05-29 since:2020-02-01 -filter:replies"
tweets = query_tweets(query) #, begindate=begin_date,
                            #    enddate=end_date)
    

print("Found: {} tweets".format(len(tweets)))


#"screen_name","username","user_id",
#"timestamp","text"
j = []
for t in tweets:
    t.timestamp = t.timestamp.isoformat()
    j.append(t.__dict__)

file = "../data/cuomo_tweets.json"

this_folder = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(this_folder, file)         

print("Wrote: {} tweets".format(len(j)))

with open(my_file, "w") as f:
    f.write(json.dumps(j))

#length_of_each.update({'2020-04-{}'.format(i):len(j)})
f.close()

