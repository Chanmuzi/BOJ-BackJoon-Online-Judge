import math

m,n = map(int,input().split())

end_index_list = [True for i in range(n+1)] # n까지 True 리스트 생성

for i in range(2,int(math.sqrt(n))+1):  # 소수는 루트 n까지만 구하면 됨
    if end_index_list[i] == True:   # 리스트에 True로 되어있으면
        for j in range(i+i,n+1,i):  # 그 index를 제외한 배수 index들을
            end_index_list[j] = False   #  n+1까지 false처리

end_num_list = []   # 공백 리스트 생성

for i in range(2,n+1):
    if end_index_list[i]:   # 해당 리스트의 i번째 요소가 참이라면
        end_num_list.append(i)  # 공백 리스트에 인덱스를 정수로 추가

for i in end_num_list:  # 최종 리스트의 요소가
    if i >= m:  # 최소값 m 이상의 숫자면
        print(i)    # 출력
