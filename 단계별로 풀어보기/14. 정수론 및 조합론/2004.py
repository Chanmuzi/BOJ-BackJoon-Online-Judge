# n,m 입력 받기
n,m = map(int,input().split())

# 약수 세기 함수
def count_measure(x,y):
    count = 0
    # 0이 될 때까지
    while x:
        x //= y
        # 나눈 몫 자체를 count
        count += x
    return count

# 5가 포함된 개수
measure_five = count_measure(n,5) - count_measure(m,5) - count_measure(n-m,5)
# 2가 포함된 개수
measure_two = count_measure(n,2) - count_measure(m,2) - count_measure(n-m,2)

# 약수가 10인 경우는 2와 5가 짝지어진 경우
measure_ten = min(measure_five, measure_two)
print(measure_ten)