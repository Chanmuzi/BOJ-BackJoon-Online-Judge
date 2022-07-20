# factorial 함수 불러오기
from math import factorial

# n,m 입력 받기
n,m = map(int,input().split())
# 이항 계수 구하기
binomial = factorial(n)//factorial(m)//factorial(n-m)

# 0 개수 초기화
count = 0
# 뒷자리부터 첫자리까지
for i in range(len(str(binomial))-1,-1,-1):
    # 0이 아니면 반복문 탈출
    if str(binomial)[i] != '0': break
    # 0이 나올때까지 count 증가
    else:
        count += 1

# count 출력
print(count)