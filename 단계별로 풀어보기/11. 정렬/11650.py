import sys

# n 입력 받기, 공백 리스트 생성
n = int(sys.stdin.readline())
dot_list = []

# 줄마다 입력받는 두 숫자를 공백 유지하여 리스트 형태로 추가
for i in range(n):
    dot_list.append(list(map(int,sys.stdin.readline().split())))

# 리스트 정렬
dot_list = sorted(dot_list)

# 리스트의 첫 번째, 두 번째 요소를 공백 포함하여 출력
for i in range(n):
    print(dot_list[i][0],dot_list[i][1])