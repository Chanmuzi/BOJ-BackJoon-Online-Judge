import math

while True:
    n = int(input())
    n = 2*n  # 입력받은 n을 두배로 변경
    if n == 0:  # n이 0이면
        break   # 반복 종료
    else:
        count = 0   # 소수의 개수 초기화
        result_list = [] # 소수가 담길 리스트
        test_list = [True for i in range(n+1)]  # True 리스트(에라토스테네스의 체)
        for i in range(2,int(math.sqrt(n))+1):  # 소수는 루트 n 범위까지 판별
            if test_list[i] == True:    # 요소가 True일 경우
                for j in range(i+i,n+1,i):  # 해당 요소를 제외한 배수를
                    test_list[j] = False    # False 처리
        for i in range(2,n+1):    # 위 리스트에서 2이상 n이하 범위에 대해
            if test_list[i]:      # i번 요소가 True인 경우(소수인 경우)
                result_list.append(i)   # 결과 리스트에 추가
        for i in result_list:   # 결과 리스트의 요소가
            if i > n/2:         # n보다 클 경우
                count += 1      # count 증가
        print(count)