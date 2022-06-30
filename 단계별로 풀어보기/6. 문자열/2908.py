import sys

a,b = sys.stdin.readline().split()
a = int(a[0]) + int(a[1])*10 + int(a[2])*100
b = int(b[0]) + int(b[1])*10 + int(b[2])*100

if a > b:
    print(a)
else: print(b)