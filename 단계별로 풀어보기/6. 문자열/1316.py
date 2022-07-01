import sys

s = int(sys.stdin.readline())
groupWordCount = 0
error = 0

for i in range(s):  # 입력받은 숫자만큼 반복
    x = sys.stdin.readline()    # 문자열 입력받기
    for j in range(len(x)-1):   # 다음 인덱스와 비교하기 위해 길이-1
        if x[j] != x[j+1]:      # 다음 문자와 다른 경우
            afterX = x[j+1:]    # 이후 모든 문자로 새로운 문자열 생성
            for k in range(len(afterX)):  
                if x[j] == afterX[k]: # 새로운 문자열에 비교 문자와 같은 것이 있다면
                    error += 1  # 에러를 추가한다
    if error == 0:  # 에러가 하나도 없는 경우에만
        groupWordCount += 1 # count를 올린다
    error = 0
print(groupWordCount)