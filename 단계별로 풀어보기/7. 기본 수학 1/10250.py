from math import floor


t = int(input())

for i in range(t):
    h,w,n = map(int,input().split())
    if n % h == 0:
        unit_num = n // h 
        floor_num = h
    else:
        unit_num = n // h + 1
        floor_num = n % h
    print(floor_num*100 + unit_num)