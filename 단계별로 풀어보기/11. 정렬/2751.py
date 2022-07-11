import sys
n = int(sys.stdin.readline())
my_list = []
# n번만큼 입력 받기
for i in range(n):
    my_list.append(int(sys.stdin.readline()))
# my_list 정렬 후 요소 하나씩 출력
for i in sorted(my_list):
    sys.stdout.write(str(i)+'\n')