import sys

myList = []

for i in range(10):
    temp = int(sys.stdin.readline())%42
    if temp not in myList:
        myList.append(temp)
    else: continue
print(len(myList))