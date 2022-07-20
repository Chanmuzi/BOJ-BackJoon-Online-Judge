# 팩토리얼 함수 불러오기
from math import factorial

# n 입력 받기
n = int(input())
# 팩토리얼 적용
factorial_n = factorial(n)

# 0개수 초기화
count = 0
# 일의 자릿수부터 최대 자릿수까지
for i in range(len(str(factorial_n))-1,-1,-1):
    # 0이 아니면 반복문 탈출
    if str(factorial_n)[i] != '0': break
    # 0이 나올때까지 count 증가
    else:
        count += 1

# count 출력
print(count)
