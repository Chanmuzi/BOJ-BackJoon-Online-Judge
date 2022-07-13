import sys

n = int(sys.stdin.readline())
# n개의 정수로 리스트 생성
num_list = list(map(int,sys.stdin.readline().split()))
# 리스트 요소로 딕셔너리 생성
num_dict = {num_list[i]:i for i in range(n)}

m = int(sys.stdin.readline())
# m개의 정수로 테스트 리스트 생성
test_list = list(map(int,sys.stdin.readline().split()))
# 리스트 요소로 딕셔너리 생성
test_dict = {test_list[i]:i for i in range(m)}

# 테스트 딕셔너리의 각 요소에 대해
for i in test_dict:
    # 숫자 딕셔너리에 존재한다면 1을 출력
    if i in num_dict: sys.stdout.write(str(1) + ' ')
    # 존재하지 않으면 0을 출력
    else: sys.stdout.write(str(0) + ' ')