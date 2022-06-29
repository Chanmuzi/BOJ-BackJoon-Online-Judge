import sys
N,X = map(int,sys.stdin.readline().split())
myList = list(map(int,sys.stdin.readline().split()))

for i in myList:
    if i < X :
        print(i,end=' ')
    else: continue
    