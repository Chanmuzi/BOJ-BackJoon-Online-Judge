from math import factorial

# n,k 입력
n,k = map(int,input().split())

# 이항 계수 출력
print(factorial(n)//factorial(k)//factorial(n-k))