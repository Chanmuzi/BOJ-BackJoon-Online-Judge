n = int(input())

def factorial(x):
    if x <= 1:  # 0!, 1!은
       return 1 # 1이다
    return x * factorial(x-1) # factorial의 정의       

print(factorial(n))