import sys

# x,y 리스트 초기화
list_x = []
list_y = []

# 입력받는 좌표 x,y를 각각 저장
x1,y1 = map(int,sys.stdin.readline().split())
x2,y2 = map(int,sys.stdin.readline().split())
x3,y3 = map(int,sys.stdin.readline().split())
list_x.extend([x1,x2,x3])
list_y.extend([y1,y2,y3])

# 정답이 되는 x,y 초기화
last_x = 0
last_y = 0

# x 리스트에 대해
for i in list_x:
    # 리스트에 요소가 1개인 경우
    if list_x.count(i) == 1:
        last_x = i
# y 리스트에 대해        
for i in list_y:
    # 리스트에 요소가 1개인 경우
    if list_y.count(i) == 1:
        last_y = i
        
print(last_x, last_y)                