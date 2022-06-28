a,b = map(int,input().split())
time = a*60 + b
alarm = time - 45
if alarm >= 0:
    print(alarm//60, alarm%60)
else: 
    alarm += 1440
    print(alarm//60, alarm%60)