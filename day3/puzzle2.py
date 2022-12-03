import string
from itertools import islice

f=open ("input.txt", "r")
totalPri = 0
matchSecond = False
matchThird = False
alreadySeen = False
bag1 = ""
bag2 = ""
bag3 = ""
count = 0
lineIteration = 0

content = f.readlines()
f.seek(0)
#get total lines
for totalLines, line in enumerate(f):
        pass
f.seek(0)
for line in f:
    if(count>=totalLines-1):
        break
    if(lineIteration == 3):
        lineIteration = 0
    alreadySeen = False
    bag1= content[count]
    bag2 = content[count+1]
    bag3 = content[count+2]
    if(lineIteration == 0): 
        for char in bag1:
            matchSecond = False
            matchThird = False
            for ch in bag2:
                if(char == ch):
                    matchSecond = True
                    break
            for ch in bag3:
                if(char==ch):
                    matchThird = True
                    break
            if(matchSecond and matchThird and not char.isspace() and not alreadySeen):
                alreadySeen = True
                if(char.islower()):
                    totalPri += string.ascii_lowercase.index(char)+ 1
                else:
                    totalPri += string.ascii_lowercase.index(char.lower()) + 26 + 1
    count+=1
    lineIteration+=1
print(totalPri)
f.close()
            
    
                        
