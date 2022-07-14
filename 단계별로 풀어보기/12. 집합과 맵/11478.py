import sys

# 입력 문자열 변수 s에 저장
s = sys.stdin.readline().rstrip()

# 부분 문자열 저장할 set 초기화
part_set = set()

# i는 부분 문자열의 길이
for i in range(1,len(s)+1):
    # j는 부분 문자열의 시작점
    for j in range(len(s)-i+1):
        part_set.add(s[j:j+i])

# set의 길이 출력
print(len(part_set))
