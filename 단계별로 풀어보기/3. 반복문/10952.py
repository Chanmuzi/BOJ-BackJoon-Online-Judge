import sys

while True:
    A,B = map(int,sys.stdin.readline().split())
    if (A and B) == 0:
        break
    print(A+B)