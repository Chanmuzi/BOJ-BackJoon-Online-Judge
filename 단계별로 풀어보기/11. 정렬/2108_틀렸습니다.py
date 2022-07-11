import sys
n = int(sys.stdin.readline())

# 양수 리스트 생성(0포함)
my_list_plus = [0]*4001
# 음수 리스트 생성(0제외)
my_list_minus = [0]*4001

for i in range(n):
    temp = int(sys.stdin.readline())
    # 입력값이 양수이면
    if temp >= 0:
        my_list_plus[temp] += 1
    # 입력값이 음수이면 절대값 인덱스
    else: my_list_minus[abs(temp)] += 1

# 총합 초기화
total = 0
# 결과 리스트 초기화
result_list = []
# 양수에 대하여
for i in range(4001):
    # 리스트 요소가 0이 아닐 때
    if my_list_plus[i] != 0:
        total += i * my_list_plus[i]
        result_list.append(i)
# 음수에 대하여, 0제외이기 때문에 range는 1부터        
for i in range(1,4001):
    if my_list_minus[i] != 0:
        total -= i * my_list_minus[i]
        result_list.append(-i)
# formatting을 통해 소수 첫째 자리에서 반올림
print('-----------------')        
print(round(total/n))
# 결과 리스트 중복 삭제 후 중간 값 출력
result_list = sorted(list(set(result_list)))
result_list_length = len(result_list)
print(result_list[result_list_length//2])


# 최빈값 양수에만 존재하는 경우
if max(my_list_plus) > max(my_list_minus):
    # 최빈값 리스트 생성
    frequent_list = list(filter(lambda x: my_list_plus[x] == max(my_list_plus), range(len(my_list_plus))))
    # 최빈값 요소가 하나라면 그것을 출력
    if len(frequent_list) == 1:
        print(frequent_list[0])
    # 하나가 아니라면 두 번째로 작은 값 출력
    else: print(frequent_list[1])
# 최빈값 음수에만 존재하는 경우    
elif max(my_list_plus) < max(my_list_minus):
    # 최빈값 리스트 생성
    frequent_list = list(filter(lambda x: my_list_minus[x] == max(my_list_minus), range(len(my_list_minus))))
    frequent_list.reverse()
    # 최빈값 요소가 하나라면 그것을 출력
    if len(frequent_list) == 1:
        print(-frequent_list[0])
    # 하나가 아니라면 두 번째로 작은 값 출력
    else: print(-frequent_list[1])
# 최빈값이 양수, 음수 둘 다 있는 경우    
else:
    # 각각을 구해 하나로 합쳐 최종 리스트 생성
    frequent_list_plus = list(filter(lambda x: my_list_plus[x] == max(my_list_plus), range(len(my_list_plus))))
    frequent_list_minus = list(filter(lambda x: my_list_minus[x] == max(my_list_minus), range(len(my_list_minus))))
    frequent_list_minus.reverse()
    # 음수 리스트를 앞에 적어야 음수값부터 오름차순으로 정렬됨
    frequent_list = frequent_list_minus + frequent_list_plus
    # 음수 리스트 요소가 1개 이하일 때는 그대로 출력
    if len(frequent_list_minus) <= 1:
        print(frequent_list[1])
    # 음수 리스트 요소가 2개 이상일 때는 음수로 출력    
    else:
        print(-frequent_list[1])


# 최대,최소값 초기화
max_value = 0
min_value = 0

# 음수 리스트는 비어 있고 양수 리스트에만 값이 있는 경우
if (max(my_list_minus) == 0) and (max(my_list_plus) != 0):
    # 양수 리스트 역순으로 확인    
    for i in range(4000,-1,-1):
        if my_list_plus[i] != 0:
            max_value = i
            break
    # 양수 리스트 정순으로 확인
    for i in range(4001):
        if my_list_plus[i] != 0:
            min_value = i
            break
# 음수 리스트에는 값이 있고 양수 리스트는 비어 있는 경우
elif (max(my_list_minus) != 0) and (max(my_list_plus) == 0):
    # 음수 리스트 정순으로 확인(음수라서 절대값이 작은 것이 최대값)
    for i in range(1,4001):
        if my_list_minus[i] != 0:
            max_value = -i
            break
    # 음수 리스트 역순으로 확인(음수라서 절대값이 큰 것이 최소값)
    for i in range(4000,0,-1):
        if my_list_minus[i] != 0:
            min_value = -i
            break
# 음수, 양수 두 리스트에 값이 있는 경우        
else:            
    # 양수 리스트를 역순으로 확인
    for i in range(4000,-1,-1):
        if my_list_plus[i] != 0:
            max_value = i
            break
    # 음수 리스트를 역순으로 확인    
    for i in range(4000,0,-1):
        if my_list_minus[i] != 0:
            min_value = -i
            break
# 최대값 - 최소값이 곧 범위
print(max_value - min_value)
