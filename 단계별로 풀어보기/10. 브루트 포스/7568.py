n = int(input())

my_list = []
# n명에 대해
for i in range(n):
    # 몸무게와 키를 튜플 형태로 리스트에 추가
    x,y = map(int,input().split())
    my_list.append((x,y))

# 덩치가 큰 사람 수를 담을 리스트
result_list = []
for i in range(n):
    # 큰 사람수 +1이 곧 등수이므로 미리 1을 부여
    count = 1
    for j in range(n):        
        # 몸무게와 키가 둘 다 큰 경우에만 count 증가
        if my_list[i][0] < my_list[j][0] and my_list[i][1] < my_list[j][1]:
                count += 1
    # 결과 리스트에 순서대로 count 추가                
    result_list.append(count)

# count를 순서대로 공백과 함께 출력
for i in result_list:
    print(i,end=' ')
        