from twitterscraper import query_tweets
import datetime as dt 
import json
import os
import time
#import time

#31 December 2019, health authorities in China reported to the World 
#The COVID-19 pandemic spread to the United States on January 19, 2020


#begin_date = dt.date(2020,2,1)
#end_date = dt.date(2020,2,2) #does not include it
#file = "march3"
#filename = "{}.json".format(file) 
#length_of_each = {}
for i in range(25,28):
    query = "cuomo -chris lang:en until:2020-05-{} since:2020-05-{} -filter:links -filter:replies".format(i+1, i)
    tweets = query_tweets(query) #, begindate=begin_date,
                                #    enddate=end_date)
        

    print("Found: {} tweets".format(len(tweets)))


    #"screen_name","username","user_id",
    #"timestamp","text"
    j = []
    for t in tweets:
        t.timestamp = t.timestamp.isoformat()
        j.append(t.__dict__)

    file = "may{}.json".format(i)

    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, file)         

    print("Wrote: {} tweets".format(len(j)))

    with open(my_file, "w") as f:
        f.write(json.dumps(j))
    
    #length_of_each.update({'2020-04-{}'.format(i):len(j)})
    f.close()

    time.sleep(120)


#automate length of each
"""
txt_file = os.path.join(this_folder, "april/length_of_each.txt") 
with open(txt_file,"w") as file:
    for key,value in length_of_each.items():
        file.write('{} : {}\n'.format(key,value))
file.close()
"""