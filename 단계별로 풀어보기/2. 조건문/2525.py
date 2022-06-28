a,b = map(int,input().split())
c= int(input())
time = a*60 + b
alarm = time + c
if alarm >= 1440:
    alarm -= 1440
    print(alarm//60, alarm%60)
elif alarm >= 0:
    print(alarm//60, alarm%60)
else: 
    alarm += 1440
    print(alarm//60, alarm%60)