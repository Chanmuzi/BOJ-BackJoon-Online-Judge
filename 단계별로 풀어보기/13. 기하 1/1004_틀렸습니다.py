# 정수 t 입력 받기
t = int(input())

# t번 반복
for i in range(t):
    # 출발점, 도착점 좌표 입력
    x1,y1,x2,y2 = map(int,input().split())
    
    # 정수 n 입력 받기
    n = int(input())
    # count 변수 초기화
    count = 0

    # n번 동안
    for i in range(n):
        a,b,r = map(int,input().split())
        # 출발점과 도착점 둘 다 원 안에 존재한다면
        if (x1-a)**2 + (y1-b)**2 < r**2 and (x2-a)**2 + (y2-b)**2 < r**2:
            continue
        # 출발점만 원 안에 존재한다면
        elif (x1-a)**2 + (y1-b)**2 < r**2:
            count += 1
        # 도착점만 원 안에 존재한다면
        elif (x2-a)**2 + (y2-b)**2 < r**2:
            count += 1

print(count)