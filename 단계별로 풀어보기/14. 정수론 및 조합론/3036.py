from fractions import Fraction

# n 입력
n = int(input())

# 반지름 입력 받아 리스트 생성
r_list = list(map(int,input().split()))

# 리스트의 첫 요소를 기준으로 나눗셈
for i in range(1,n):
    if r_list[0] % r_list[i] == 0:
        print(f'{r_list[0]//r_list[i]}/1')
    else: print(Fraction(r_list[0],r_list[i]))
