from twitterscraper import query_tweets
import datetime as dt 
import json
import os
import time
#import time



#begin_date = dt.date(2020,2,1)
#end_date = dt.date(2020,2,2) #does not include it
#file = "march3"
#filename = "{}.json".format(file) 
#length_of_each = {}
for i in range(1,31):
    query = "cuomo -chris lang:en until:2020-05-{} since:2020-05-{} -filter:links -filter:replies".format(i+1, i)
    tweets = query_tweets(query) 

    print("Found: {} tweets".format(len(tweets)))


    j = []
    for t in tweets:
        t.timestamp = t.timestamp.isoformat()
        j.append(t.__dict__)

    file = "may/may{}.json".format(i)

    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, file)         

    print("Wrote: {} tweets".format(len(j)))

    with open(my_file, "w") as f:
        f.write(json.dumps(j))
    
    #length_of_each.update({'2020-04-{}'.format(i):len(j)})
    f.close()

    time.sleep(120)


#automate length of each
