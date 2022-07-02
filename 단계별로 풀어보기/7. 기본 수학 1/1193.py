n = int(input())
number = 1
count = 1

if n == 1:
    print("1/1")
else: 
    while n > number:
        count += 1
        number += count
    remainder = number % n

    if count % 2 == 0:
        head = count - remainder
        tail = 1 + remainder
    else:
        head = 1 + remainder
        tail = count - remainder
    
    print(f'{head}/{tail}')