# 두 자연수 입력 받기
a,b = map(int,input().split())

# 둘 중에 더 작은 값부터 1까지 역순으로
for i in range(min(a,b),0,-1):
    # 두 수를 i로 나눈 나머지가 둘 다 0일 때
    if a % i == 0 and b % i == 0:
        # 최대공약수 출력 및 반복 중단
        print(i)
        # 최대공약수 저장
        gcd = i
        break
# 최소공배수 출력
# 최소공배수는 (두 수의 곱) // (최대공약수)
print(a*b//gcd)