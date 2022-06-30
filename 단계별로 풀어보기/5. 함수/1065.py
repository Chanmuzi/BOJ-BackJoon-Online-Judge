import sys

n = int(sys.stdin.readline())
count = 0

if n < 100:
    print(n)
elif 100 <= n < 1000:
    for i in range(100,n+1):
        a,b,c = map(int,str(i))
        if a-b == b-c:
            count+=1
    print(count+99)
else: print(144)