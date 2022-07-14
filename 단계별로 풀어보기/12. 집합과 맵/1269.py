import sys

# a,b 나눠서 정수로 입력 받기
a,b = map(int,sys.stdin.readline().split())

# 정수 a개 set으로 저장
set_A = set(map(int,sys.stdin.readline().split()))
# 정수 b개 set으로 저장
set_B = set(map(int,sys.stdin.readline().split()))

# 차집합 구하기
difference_A = set_A - set_B
difference_B = set_B - set_A

# 대칭 차집합 원소 개수 출력
print(len(difference_A) + len(difference_B))