import sys
n = int(sys.stdin.readline())

# 자연수 n의 범위를 고려하여 리스트에 10001개 항목 생성
# 인덱스는 0부터 시작이므로 10001까지 생성
my_list = [0]*10001

# 입력받은 숫자를 인덱스로 활용하여 +1
for i in range(n):
    my_list[int(sys.stdin.readline())] += 1

# 0인 요소는 제외하고 count된만큼 해당 숫자 출력
for i in range(10001):
    if my_list[i] != 0:
        for j in range(my_list[i]):
            sys.stdout.write(str(i)+'\n')