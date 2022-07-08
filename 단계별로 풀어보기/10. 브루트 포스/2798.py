n,m = map(int,input().split())

my_list = list(map(int,input().split())) # n개의 숫자를 리스트에 입력

temp_list = []  # 결과값들을 담을 공백 리스트 생성

for i in range(n):  # 1번값
    for j in range(i+1,n):  # 2번값
        for k in range(j+1,n):  # 3번값
            # 세 값의 합이 m 이하일 때만
            if my_list[i] + my_list[j] + my_list[k] <= m:   
                # 리스트에 추가
                temp_list.append(my_list[i] + my_list[j] + my_list[k])

# 리스트의 최대값 출력                            
print(max(temp_list))