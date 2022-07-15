# 계속 반복
while True:
    a,b = map(int,input().split())
    # 0,0 이 입력되면 반복 종료
    if (a,b) == (0,0): break
    # b를 a로 나눈 나머지가 0이라면
    elif b % a == 0: print('factor')
    # a를 b로 나눈 나머지가 0이라면
    elif a % b == 0: print('multiple')
    # 둘 다 아니라면
    else: print('neither')