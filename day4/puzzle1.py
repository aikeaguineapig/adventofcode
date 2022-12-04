import re

count = 0
f=open ("input.txt", "r")
lines = f.readlines()
for line in lines:
    [a0,a1,b0,b1] = re.split(',|-|\n',line)[:4]
    count += ((int(a0)>=int(b0) and int(a1)<=int(b1)) or (int(b0)>=int(a0) and int(b1)<=int(a1)))
print(count)
