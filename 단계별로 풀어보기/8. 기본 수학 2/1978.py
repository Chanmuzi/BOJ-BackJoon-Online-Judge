n = int(input())
my_list = map(int,input().split())
count = 0
temp = 0

for i in my_list:
    if i == 1: continue
    elif i <= 3:  # 범위 설정 때문에 3 이하 자연수는 전부 소수로 미리 count
        count += 1
    else:
        for j in range(2,i):
            if i % j == 0:                
                temp += 1   # 1과 자신을 제외한 다른 값으로 딱 떨어지는 개수
        if temp == 0: count += 1    # 딱 떨어지는 수가 없을 때만
        temp = 0   # 임시값 초기화
print(count)