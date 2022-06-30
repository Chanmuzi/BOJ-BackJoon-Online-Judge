import sys

N = int(sys.stdin.readline())   # 변수 N에 정수를 입력받는다.
cycle = 0
nextN = N

while True:
    cycle += 1
    if nextN < 10:  # 연산 수행 결과가 10보다 작으면
        nextN = 11*nextN    # 11을 곱한다
    else:
        nextN = (nextN%10*10)+(nextN//10+nextN%10)%10   
    if nextN == N:  # 연산 수행 후 초기값과 동일하면
        break       # 반복을 종료한다
print(cycle)