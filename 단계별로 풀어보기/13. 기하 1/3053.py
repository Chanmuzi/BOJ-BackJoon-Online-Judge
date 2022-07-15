import math

# 반지름 입력 받기
r = int(input())

# 유클리드 기하학 원의 넓이
s1 = math.pi * r ** 2
print(f'{s1:.6f}')

# 택시 기하학 원의 넓이
s2 = (2 * r) ** 2 // 2
print(f'{s2:.6f}')