# Python program to read 
# json file 
  
  
import json 

import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'may/may1.json')  
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
    counter += 1 
    print(i['text'])
    print(i['timestamp'])
    print("="*23)
        #print(i['screen_name'])
    # print(i['])
   # if counter == 10:
   #     break
   
        

print(counter)
print(my_file)
# Closing file 
f.close() 
