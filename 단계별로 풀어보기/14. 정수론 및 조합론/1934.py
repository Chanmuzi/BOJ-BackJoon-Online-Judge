import sys
import math

# 정수 t 입력
t = int(sys.stdin.readline())

# t번 반복
for i in range(t):
    # a,b 입력
    a,b = map(int,sys.stdin.readline().split())
    # 최소공배수 출력
    print(math.lcm(a,b))