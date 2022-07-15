# 진짜 약수 개수 입력 받기
num = int(input())

# 진짜 약수 리스트에 저장하기
num_list = list(map(int,input().split()))
# 진짜 약수 리스트 오름차순 정렬
num_list.sort()

# 진짜 약수의 개수가 1이라면
if num == 1: print(num_list[0]**2)
# 나머지 경우는 가장 작은 수와 가장 큰 수를 곱해서 출력
else: print(num_list[0] * num_list[len(num_list)-1])