import sys

C = int(sys.stdin.readline())

for i in range(C):  # C만큼 반복
    # 입력 받은 내용을 정수로 변환해 list 생성
    tempList = list(map(int,sys.stdin.readline().split()))
    tempSum = 0     # 임시 변수 초기화
    overAverage = 0
    for i in range(1,len(tempList)):    # 리스트의 첫 번째 요소를 제외하고
        tempSum += tempList[i]
    tempAverage = tempSum / (len(tempList)-1)   # 평균 구하기
    for j in range(1,len(tempList)):    # 리스트의 첫 번째 요소를 제외하고
        if tempList[j] > tempAverage:   # 평균보다 크다면
            overAverage += 1            # 한 개 증가
    percentage = overAverage / (len(tempList)-1) * 100
    print(f'{percentage:.3f}%')