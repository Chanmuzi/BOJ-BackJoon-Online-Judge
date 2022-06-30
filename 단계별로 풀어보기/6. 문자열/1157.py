import sys

s = sys.stdin.readline()
s = s.upper()   # 대문자로 변경. 반드시 변수에 새로 할당해줘야 함
myList = []

for i in range(ord("A"),ord("A")+26):   # 유니코드 숫자로 범위를 정한다
    myList.append(s.count(chr(i)))      # myList에 문자의 개수를 세서 추가한다
    
maxNum = max(myList)
maxCount = 0
maxIndex = []

for j in range(len(myList)):
    if myList[j] == maxNum: # myList의 j번째 값이 최댓값이라면
        maxCount += 1       # count를 올려주고
        maxIndex.append(j)  # 몇 번인지 maxIndex에 기록한다
        
if maxCount == 1:   # 최댓값이 유일하게 존재할 때만
    print(chr(maxIndex[0]+ord("A")))    # 대문자를 출력한다
else: print("?")