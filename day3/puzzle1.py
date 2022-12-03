import string

f=open ("input.txt", "r")
compartment1= ""
compartment2 = ""
totalPri = 0
match = False
seen = ""
alreadySeen = False


for line in f:
    #split string
    compartment1=""
    compartment2=""
    seen = ""
    for i in range(0,len(line)):
        if i <= len(line)//2-1:
            compartment1 = compartment1 + line[i]
        else:
            compartment2 = compartment2 + line[i]
    for char in compartment1:
        match = False
        alreadySeen = False
        for ch in seen:
            if(char == ch):
                alreadySeen = True
        for ch in compartment2:
            if(char==ch):
                match = True
        if(match and not alreadySeen):
            seen += char
            if(char.islower()):
                totalPri += string.ascii_lowercase.index(char)+ 1
            else:
                totalPri += string.ascii_lowercase.index(char.lower()) + 26 + 1
print(totalPri)
            
    
                        
