import sys

s = int(sys.stdin.readline())
groupWordCount = 0
error = 0

for i in range(s):
    x = sys.stdin.readline()
    for j in range(len(x)-1):
        if x[j] != x[j+1]:
            afterX = x[j+1:]
            for k in range(len(afterX)):
                if x[j] == afterX[k]:
                    error += 1
    if error == 0:
        groupWordCount += 1
    error = 0
print(groupWordCount)