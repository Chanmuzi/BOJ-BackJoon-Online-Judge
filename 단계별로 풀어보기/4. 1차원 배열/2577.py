import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
result = str(A * B * C)     # 인덱스를 적용하기 위해 문자열로 변환
myList = []     # 공백 리스트 생성

for i in range(len(result)):   # 문자열 길이에 대하여
    myList.append(int(result[i]))   # 각 문자를 정수로 변환해 리스트에 추가

for j in range(10): # 0부터 10까지
    print(myList.count(j))  # 리스트 안의 개수를 세어 출력