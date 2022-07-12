n = input()
# 공백리스트 초기화
my_list = []

# 입력받은 문자열을 정수로 리스트에 입력
for i in range(len(n)):
    my_list.append(int(n[i]))

# 리스트 내림차순 정렬
my_list.sort(reverse=True)

# 리스트 각 요소를 줄을 바꾸지 않고 출력
for i in my_list:
    print(i, end='')