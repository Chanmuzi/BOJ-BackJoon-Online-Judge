from math import factorial

# t 입력
t = int(input())

# t번 반복
for i in range(t):
    # n,m 입력
    n,m = map(int,input().split())
    print(factorial(m)//factorial(n)//factorial(m-n))