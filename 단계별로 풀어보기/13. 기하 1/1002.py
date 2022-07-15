# 두 점 사이의 거리를 구하는 함수
def distance(x1, y1, x2, y2):
    d = ((x2-x1)**2 + (y2-y1)**2)
    return d

# t 정수로 입력 받기
t = int(input())
# 두 원 정보를 담을 리스트 초기화
c1 = []
c2 = []
# t번 반복
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    c1.append((x1, y1, r1))
    c2.append((x2, y2, r2))
    # 두 원의 좌표로 거리 구하는 함수에 적용    
    D = distance(x1, y1, x2, y2)

    # 동심원일 때
    if D == 0:
        # 동일한 두 원이라면
        if r1 == r2:
            print(-1)
        # 겹치지 않는 두 원이라면
        else: print(0)
    # 두 점에서 만날 때
    elif (r1-r2)**2 < D and D < (r1+r2)**2:
        print(2)
    
    # 한 점에서 만날 때
    elif (r1+r2)**2 == D or (r1-r2)**2 == D:
        print(1)
    
    # 만나지 않을 때
    elif (r1+r2)**2  < D or D < (r1-r2)**2:
         print(0)