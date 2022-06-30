import sys
s = sys.stdin.readline()

numList = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time = 0

for i in range(len(s)):
    for j in range(len(numList)):
        for k in range(len(numList[j])):
            if s[i] == numList[j][k]:
                time += (j+3)
print(time)