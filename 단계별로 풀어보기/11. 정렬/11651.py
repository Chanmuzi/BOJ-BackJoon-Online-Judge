import sys

# n 입력 받기, 공백 리스트 생성
n = int(sys.stdin.readline())
dot_list = []

for i in range(n):
    # 숫자 두 개를 x,y 변수에 저장
    x,y = map(int,sys.stdin.readline().split())
    # y,x 순서로 리스트를 만들어 공백 리스트에 추가
    dot_list.append([y,x])

# y 기준으로 리스트 정렬
dot_list = sorted(dot_list)

# x,y 출력
for i in range(n):
    print(dot_list[i][1],dot_list[i][0])