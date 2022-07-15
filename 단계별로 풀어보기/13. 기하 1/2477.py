import sys

# k 입력 받기
k = int(input())
# 방향, 이동거리 리스트로 저장
values = [input().split() for _ in range(6)]
# 방향 리스트
directions = [int(v[0]) for v in values]
# 길이 리스트
lengths = [int(v[1]) for v in values]
# 큰 상자, 작은 상자 길이 리스트 초기화
big_lengths, small_lengths = [], []

# 동서남북 중
for i in range(1, 5):
    # 한번만 입력되었다면
    if directions.count(i) == 1:
        # 큰 상자의 변으로 추가
        big_lengths.append(lengths[directions.index(i)])
        # 작은 상자의 인덱스 설정
        temp = directions.index(i) + 3
        # 인덱스는 0~5 범위로 맞춰주기
        if temp >= 6:
            temp -= 6 
        # 작은 상자의 변으로 추가
        small_lengths.append(lengths[temp]) 

# 전체 면적 = 큰 상자 - 작은 상자
s = big_lengths[0] * big_lengths[1] - small_lengths[0] * small_lengths[1]
print(k * s)