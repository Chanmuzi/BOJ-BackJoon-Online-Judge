import math

# 두 자연수 입력 받기
a,b = map(int,input().split())
# 최대공약수 출력
print(math.gcd(a,b))
# 최소공배수 출력
print(math.lcm(a,b))