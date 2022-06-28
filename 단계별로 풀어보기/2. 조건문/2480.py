myList = list(map(int,input().split()))
myList.sort()
count = 0

if myList[0] == myList[1] or myList[0] == myList[2]:
    count += 1
    if myList[1] == myList[2]:
        count += 1
else:
    if myList[1] == myList[2]:
        count += 1

if count == 0:
    print(max(myList)*100)
elif count == 1:
    print(1000 + myList[1]*100)    
else: print(10000 + myList[0]*1000)