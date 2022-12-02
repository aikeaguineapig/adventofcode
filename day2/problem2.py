f=open ("input.txt", "r")
theirChoice = ""
myChoice = ""
score = 0
for line in f:
    theirChoice = line[0]
    myChoice= line[2]
    #print(myChoice, theirChoice)
    if(myChoice =='X'):
        if(theirChoice == 'A'):
            score += 3
        if(theirChoice == 'B'):
            score += 1
        if(theirChoice == 'C'):
            score += 2
    if(myChoice == 'Y'):
        if(theirChoice == 'A'):
            score += 3 + 1
        if(theirChoice == 'B'):
            score += 3+2
        if(theirChoice == 'C'):
            score += 3 + 3
    if(myChoice =='Z'):
        if(theirChoice == 'A'):
            score += 6+2
        if(theirChoice == 'B'):
            score += 6 + 3
        if(theirChoice == 'C'):
            score += 6 + 1

print(score)
