n = int(input())

my_list = []
for i in range(1,n): # 1부터 n-1까지
    temp_list = []
    # i의 각 자릿수를 다 더하기 위해 길이를 파악
    for j in range(len(str(i))):  
        # i의 각 자릿수의 값을 리스트 추가
        temp_list.append(int(str(i)[j]))
    # i 자체도 리스트에 추가    
    temp_list.append(i)
    # 리스트에 포함된 값들의 함을 my_list에 요소로 전달
    my_list.append(sum(temp_list))

# 리스트에 생성자가 존재한다면
if n in my_list:
    # 생성자의 index 반환
    answer_index = my_list.index(n)
    # index이므로 +1 하여 출력
    print(answer_index + 1)
# 생성자가 존재하지 않는다면
else: print(0)