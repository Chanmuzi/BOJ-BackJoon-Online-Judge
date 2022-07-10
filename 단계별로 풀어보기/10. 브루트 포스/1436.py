n = int(input())

def numbering(x):
    start = 666
    # x번 수행
    for i in range(x):
        while True:
            start += 1
            # 666이 들어있을 때까지 +1 반복
            if "666" in str(start):
                break
    # x번째를 구하면 start 값을 return                
    return start

# 시작값이 666이므로 n-1을 인수로 전달
print(numbering(n-1))