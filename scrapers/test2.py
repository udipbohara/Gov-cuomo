# Python program to read 
# json file 
  
  
import json 

import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'test_cuomo.json')  
# Opening JSON file 
f = open(my_file,"r") 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  
# Iterating through the json 
# list 
print(len(data))
counter = 0 
for i in data:
    if 'cuomo' in i['text']:
        counter += 1 
        print(i['text'])
        print("="*23)
        #print(i['screen_name'])
    # print(i['])
        

print(counter)
# Closing file 
f.close() 