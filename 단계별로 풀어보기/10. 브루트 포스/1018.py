n,m = map(int,input().split())
input_list = []
# n만큼 입력 받기
for i in range(n):
    input_list.append(list(map(str,input())))

# 흰,검으로 시작하는 리스트
answer_list_W = []
answer_list_B = []
# 8행 리스트에 8개 열 '0'으로 채우기
for i in range(8):
    answer_list_W.append([])
    answer_list_B.append([])
    for j in range(8):
        answer_list_W[i].append(0)
        answer_list_B[i].append(0)

# 홀수 짝수 규칙에 맞게 "W","B" 채우기
for i in range(0,8,2):
    for j in range(0,8,2):
        answer_list_W[i][j] = "W"
        answer_list_B[i][j] = "B"
    for k in range(1,8,2):
        answer_list_W[i][k] = "B"
        answer_list_B[i][k] = "W"                
for i in range(1,8,2):
    for j in range(0,8,2):
        answer_list_W[i][j] = "B"
        answer_list_B[i][j] = "W"
    for k in range(1,8,2):
        answer_list_W[i][k] = "W"
        answer_list_B[i][k] = "B"

# 각 케이스 별로 카운트 값 넣을 리스트
count_number_W = []
count_number_B = []

# 열 기준 [n-7] 인덱스까지 시작점
for i in range(n-7):
    # 행 기준 [m-7] 인덱스까지 시작점
    for j in range(m-7):
        temp_count_W = 0
        temp_count_B = 0
        # 8 x 8 정답 체스판이랑 비교
        for k in range(8):
            for l in range(8):
                if input_list[i+k][j+l] != answer_list_W[k][l]:
                    temp_count_W += 1
                if input_list[i+k][j+l] != answer_list_B[k][l]:
                    temp_count_B += 1
        # 정답판과 다른 문자의 개수를 count한 후 리스트에 추가                    
        count_number_W.append(temp_count_W)
        count_number_B.append(temp_count_B)

# count 리스트에서 최소값 구하기
min_W = min(count_number_W)
min_B = min(count_number_B)

# 둘 중 더 작은 값 출력
print(min(min_W, min_B))