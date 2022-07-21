from random import sample
from math import factorial
# n,m 입력 받기
n,m = map(int,input().split())

# 구해야 되는 총 경우의 수
total_case = factorial(n)//factorial(n-m)
# 수열 리스트 초기화
p_list = []
# n까지의 정수 리스트
range_n = [x for x in range(1,n+1)]

# 수열이 총 경우의 수가 될 때까지    
while len(p_list) != total_case:
    # n까지의 정수중 m개를 랜덤으로 골라서
    temp = sample(range_n,m)
    # 수열 리스트에 없을 때만 추가
    if temp not in p_list: p_list.append(temp)

# 수열 리스트 오름차순 정렬    
p_list.sort()

# 수열 리스트의 각 요소(리스트)에 대하여
for i in p_list:
    # 각 리스트의 각 요소들에 대하여
    for j in i:
        # 띄어쓰기와 함께 출력
        print(j,end=' ')
    # 줄바꿈    
    print()