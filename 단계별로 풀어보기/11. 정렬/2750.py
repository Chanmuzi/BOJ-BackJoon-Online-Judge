n = int(input())

# 입력을 n번 받아 리스트에 정수형으로 추가
my_list = []
for i in range(n):
    my_list.append(int(input()))

# 리스트 오름차순 정렬
my_list.sort()
# 각 요소 출력
for i in range(n):
    print(my_list[i])