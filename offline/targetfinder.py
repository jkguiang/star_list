target = str(input("What target would you like information on? "))


with open("2016B.txt", "r") as f:
    searchlines = f.readlines()
    print("Here is what we have for", target, "on the 2016B run:")
for i, line in enumerate(searchlines):
    if target in line: 
        for l in searchlines[i:i+11]:
            print(l)

    
with open("2017A.txt", "r") as f1:
    searchlines = f1.readlines()
    print("Here is what we have for", target, "on the 2017A run:")
for i, line in enumerate(searchlines):
    if target in line: 
        for l in searchlines[i:i+11]:
            print(l)
       

with open("2017B.txt", "r") as f3:
    searchlines = f3.readlines()
    print("Here is what we have for", target, "on the 2017B run:")
for i, line in enumerate(searchlines):
    if target in line: 
        for l in searchlines[i:i+11]:
            print(l)
      
            
with open("2018A.txt", "r") as f2:
    searchlines = f2.readlines()
    print("Here is what we have for", target, "on the 2018A run:")
for i, line in enumerate(searchlines):
    if target in line: 
        for l in searchlines[i:i+11]:
            print(l)
