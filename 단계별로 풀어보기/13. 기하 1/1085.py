import sys

# x,y,w,h를 나눠서 정수로 저장
x,y,w,h = map(int,sys.stdin.readline().split())

distance_x = w - x
distance_y = h - y

print(min(x,y,distance_x,distance_y))