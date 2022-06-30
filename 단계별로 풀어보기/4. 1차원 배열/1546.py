import sys

N = int(sys.stdin.readline())
myList = list(map(int,sys.stdin.readline().split()))
maxNum = max(myList)

for i in range(N):
     myList[i] = myList[i]/maxNum*100

sum = 0
for j in myList:
    sum += j

print(sum/N)