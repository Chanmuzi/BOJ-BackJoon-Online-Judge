import sys

N = int(sys.stdin.readline())
temp = 0
count = 0

for i in range(N):
    temp = 0
    count = 0
    myString = sys.stdin.readline()
    if myString[0] == "O":
        temp += 1
        count += temp
    for j in range(len(myString)-1):
        if myString[j+1] == "O":
            temp += 1
            count += temp
        else: 
            temp = 0
    print(count)