from itertools import *

# n,m 입력
n,m = map(int, input().split())

# 순열 생성 후 출력
for p in permutations(range(1, 1 + n), m):
    print(*p)