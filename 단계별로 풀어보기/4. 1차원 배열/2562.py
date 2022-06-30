import sys

myList = []

for i in range(9):
    myList.append(int(sys.stdin.readline()))

for j in range(9):
    if myList[j] == max(myList):
        print(max(myList))
        print(j+1)