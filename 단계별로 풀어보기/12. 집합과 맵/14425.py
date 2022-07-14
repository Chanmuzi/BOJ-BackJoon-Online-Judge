import sys
# n,m 정수로 입력받기
n,m = map(int,sys.stdin.readline().split())

# n번만큼 입력 받아 딕셔너리에 딕셔너리에 추가
answer_dict = {}
for i in range(n):
    answer_dict[sys.stdin.readline().rstrip()]=i

# m번만큼 문자열 입력 받기
count = 0
for i in range(m):
    test_string = sys.stdin.readline().rstrip()
    # 문자열이 정답 딕셔너리에 있다면 count 증가
    if test_string in answer_dict: count += 1

# count 출력
print(count)
