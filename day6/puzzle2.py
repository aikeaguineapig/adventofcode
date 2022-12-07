def checkAllUnique(x):
    unique = False
    for i in range (len(x)):
        if(x.count(x[i])==1):          
            unique = True
        else:
            unique = False
            break
    return unique
f= open("input.txt", "r")
lines = f.readlines()
fourteen = []
count = 0
marker = ""
for line in lines:
    for ch in line:
        count+=1
        #if max elements
        if(len(fourteen)==14):
            fourteen.pop(0)
            fourteen.append(ch)
            #check if unique
            if(checkAllUnique(fourteen)):
                marker = fourteen
                break
                
        else:
            fourteen.append(ch)
print(marker)
print(count)
