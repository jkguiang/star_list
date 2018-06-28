import os
import json
import time
import random

pseudo_epoch = int(time.time()) 
people = ["Alice", "Bob", "Sam", "Todd", "Eve"]
db = {}

for i in range(0, 100):
    star_name = "star_{0}".format(i)
    t = random.randint(pseudo_epoch - 10000, pseudo_epoch)
    file_name = "{0}.txt".format(t)
    filt_used = "filter_{0}".format(i)
    observer = people[random.randint(0, len(people) - 1)]

    db[t] = {"name":star_name, "file":file_name, "filter":filt_used, "observer":observer}

with open("{0}/database.json".format(os.getcwd()), "w") as fout:
    json.dump(db, fout, indent=4)
    
