# t 입력
t = int(input())

# t번 반복
for i in range(t):
    # 의상 수 n 입력
    clothes_num = int(input())
    # 옷 이름 리스트
    clothes_list = []
    # 옷 종류 리스트
    sort_list = []
    # 옷 종류별 개수 리스트
    count_list = []
    # 의상 수만큼 반복
    for i in range(clothes_num):
        # 옷 이름과 종류를 나누어 리스트에 저장
        cloth,sort = input().split()
        clothes_list.append(cloth)
        sort_list.append(sort)
    # 옷 종류 리스트 중복 제거    
    sort_set = set(sort_list)
    # 각 옷 종류에 대해
    for i in sort_set:
        # 개수를 파악하여 옷 종류별 개수 리스트에 추가
        count_list.append(list(filter(lambda x:sort_list[x] == i, range(len(sort_list)))))
    # 곱셈을 위해 case 1로 초기화    
    case = 1
    # 옷 종류별 개수에 1 더한 값을 모두 곱하기
    for i in count_list:
        case *= len(i)+1
    print(case-1)