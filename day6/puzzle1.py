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
four = []
count = 0
marker = ""
for line in lines:
    for ch in line:
        count+=1
        #if max elements
        if(len(four)==4):
            four[0]= four[1]
            four[1] = four[2]
            four[2] = four[3]
            four[3] = ch
            #check if unique
            if(checkAllUnique(four)):
                marker = four
                break
                
        else:
            four.append(
print(marker)
print(count)
