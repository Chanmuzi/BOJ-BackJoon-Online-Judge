import math

# n 입력
n = int(input())
# 정수 n개 입력
num_list = list(int(input()) for _ in range(n))
# 숫자 리스트 오름차순 정렬
num_list.sort()
# 간격, 정답 리스트 초기화
interval_list = []
answer_list = []

# 입력 받은 숫자들의 차를 간격 리스트에 저장
for i in range(1, n):
    interval_list.append(num_list[i] - num_list[i - 1])

# 간격 리스트의 요소들 간의 최대 공약수를 반복문을 통해 구함
prev = interval_list[0]
for i in range(1, len(interval_list)):
    # 최대공약수 함수
    prev = math.gcd(prev, interval_list[i])

for i in range(2, int(math.sqrt(prev)) + 1): #제곱근까지만 탐색
    # 최대공약수의 약수 구하기
    if prev % i == 0:
        # 나머지가 0일 경우 약수이므로 추가
        answer_list.append(i)
        # 그 약수로 나눈 값(반대쌍)도 추가
        answer_list.append(prev//i)
# 최대공약수 자신 추가        
answer_list.append(prev)
# 중복 제거
answer_list = list(set(answer_list))
answer_list.sort()
# 모든 요소 출력
print(*answer_list)