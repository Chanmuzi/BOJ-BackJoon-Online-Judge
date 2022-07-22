from itertools import combinations

# n,m 입력
n,m = map(int, input().split())

# 조합 생성 후 출력
for x in combinations(range(1, 1 + n), m):
    print(*x)