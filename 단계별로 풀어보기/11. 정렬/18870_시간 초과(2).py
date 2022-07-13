import sys

n = int(sys.stdin.readline().rstrip())
# 입력받는 숫자들을 정수로 변환하여 리스트에 추가
num_list = list(map(int,sys.stdin.readline().split()))
# 숫자리스트의 중복을 제거하고 리스트로 재변환 후 오름차순 정렬
sorted_list = sorted(list(set(num_list)))

# 정렬된 리스트의 인덱스를 찾아 출력
for i in range(n):
    # sys 모듈의 출력함수를 사용하고 공백을 추가
    sys.stdout.write(str(sorted_list.index(num_list[i]))+' ')