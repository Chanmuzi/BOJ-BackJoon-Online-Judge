import math

def is_prime(x):    # 소수 판별식
    if x < 2:       # x가 2보다 작으면
        return False# 소수가 아니다
    for i in range(2,int(math.sqrt(x))+1):  # 소수는 루트 x 범위까지만 조사
        if x % i == 0:  # 나머지가 0인 나눗셈이 존재하면
            return False    # 소수가 아니다
    return True     # 나머지가 0인 나눗셈이 없으므로 소수

t = int(input())

for i in range(t):
    n = int(input())
    a = n//2
    b = n//2
    for j in range(n//2): # 입력된 n의 절반만큼 반복
        if is_prime(a) and is_prime(b): # a와 b 둘 다 소수일 때만
            print(a,b)  # a,b를 출력하고
            break       # 반복 종료
        else:           # a와 b 중 하나라도 소수가 아니면
            a -= 1      # 한 쪽은 값을 줄이고
            b += 1      # 한쪽은 값을 늘린다(a+b = n 유지)