t = int(input())

for i in range(t):
    h,w,n = map(int,input().split())
    if n % h == 0:  # 나머지가 0이면 최고층에 있음을 의미
        unit_num = n // h # 몫 그 자체가 호수
        floor_num = h     # 높이 자체가 층수
    else:
        unit_num = n // h + 1   # 몫에 1을 더한 값이 호수
        floor_num = n % h       # 나머지 자체가 층수
    print(floor_num*100 + unit_num) # 호수 표현을 위한 계산