import sys

N = int(sys.stdin.readline())
myList = list(map(int,sys.stdin.readline().split()))
print(min(myList),max(myList))