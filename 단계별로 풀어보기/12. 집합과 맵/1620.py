import sys

# n,m 정수로 입력받기
n,m = map(int,sys.stdin.readline().split())

# n번만큼 입력 받아 정답 딕셔너리에 추가
answer_dict = {}
for i in range(1,n+1):
    temp_string = sys.stdin.readline().rstrip()
    # key:value 추가
    answer_dict[temp_string]=str(i)
    # value:key 추가
    answer_dict[str(i)]= temp_string

# m번만큼 입력 받기
for i in range(m):
    test_string = sys.stdin.readline().rstrip()
    print(answer_dict[test_string])