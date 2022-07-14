import sys

# n,m 정수로 나누어 입력 받기
n,m = map(int,sys.stdin.readline().split())

# 듣도 못한 사람 딕셔너리 생성
hear_dict = {}
for i in range(n):
    hear_dict[sys.stdin.readline().rstrip()] = i
    
# 보도 못한 사람 딕셔너리 생성
see_dict = {}
for i in range(m):
    see_dict[sys.stdin.readline().rstrip()] = i

# 듣보잡 딕셔너리에 초기화
hear_see_list = []
# 보도 못한 사람이
for i in see_dict:
    # 듣도 못한 사람이기도 하다면
    if i in hear_dict:
        # 듣보잡 리스트에 추가
        hear_see_list.append(i)

# 듣보잡 리스트 길이 출력
print(len(hear_see_list))
# 듣보잡 리스트 정렬 후 각 요소 출력
for i in sorted(hear_see_list):
    sys.stdout.write(i + '\n')