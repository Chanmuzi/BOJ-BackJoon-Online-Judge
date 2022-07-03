n = int(input())

max_five = n//5
num_three = 0

if n % 5 == 0: print(max_five)  # n이 5로 나누어 떨어질 경우
else:
    while max_five > 0: # n을 5로 나눈 몫이 0이 될 때까지
        if (n-(max_five*5)) % 3 == 0: break # 나머지가 3의 배수이면 break
        else:
            max_five -= 1   # 나머지가 3의 배수가 될 때까지
            
    num_three = ((n - (max_five*5)) / 3)  # n에 5를 최대한 넣고 나머지를 3으로 나눈다
    if num_three == int(num_three): # 그 값이 정수이면
        print(int(max_five + num_three))
    else: print(-1) # 정수가 아니면, 즉 3으로도 나누어 떨어지지 않는다면
