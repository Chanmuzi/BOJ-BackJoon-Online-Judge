m = int(input())
n = int(input())

my_list = []

for i in range(m,n+1):  # m부터 n까지
    error = 0
    if i > 1: # 1은 포함하지 않는다
        for j in range(2,i-1): # 2부터 i-1까지
            if i % j == 0:  # i를 j로 나눈 나머지가 0이면(소수가 아니면)
                error += 1  # 
                break
        if error == 0: # error가 없으면
            my_list.append(i)
            
if len(my_list) > 0: # 공백 리스트가 아니라면
    print(sum(my_list)) # 리스트 요소의 총합
    print(min(my_list)) # 리스트의 최소값
else: print(-1)