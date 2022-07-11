import sys
from collections import Counter

# 정수를 변수 n에 저장
n = int(sys.stdin.readline())
# 입력값들을 저장할 리스트 초기화
numbers = []

for i in range(n):
    numbers.append(int(sys.stdin.readline()))

# 리스트 오름차순 정렬
numbers.sort()

# 산술평균: 리스트 총합을 n개로 나눈 값
print(round(sum(numbers)/n))

# 중앙값: n은 홀수이므로 2로 나눈 몫을 인덱스로 사용
print(numbers[n//2])

# 리스트 내 빈도 가장 높은 값 두개 가져오기
# : 작은 것부터 튜플로 가져온다
cnt = Counter(numbers).most_common(2)
# numbers의 길이가 2 이상이면서
if len(numbers) > 1:
    # 최고 빈도 두 요소의 빈도가 같다면
    if cnt[0][1] == cnt[1][1]:
        # 두 번째로 작은 요소 출력
        print(cnt[1][0])
    # 첫 요소의 빈도가 더 높다면
    else:
        # 첫 번째 요소 출력
        print(cnt[0][0])
# number의 길이가 1이면        
else:
    # 해당 요소 출력
    print(cnt[0][0])

# 범위: 최대값 - 최소값
print(max(numbers) - min(numbers))