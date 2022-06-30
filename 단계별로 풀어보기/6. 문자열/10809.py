import sys
s = sys.stdin.readline()
alphaList = []  # 공백 리스트 생성

for i in range(26):
    alphaList.append(-1)    # 공백 리스트에 -1 26개 추가
    
alphabet = 'abcdefghijklmnopqrstuvwxyz' # 알파벳 26개 문자열로 작성

for i in range(26): # 각 알파벳에 대하여
    for j in range(len(s)): # 문자열의 길이에 대하여
        if alphabet[i] == s[j]: # i번 째 알파벳이 문자열의 j번째 문자와 같다면
            if alphaList[i] == -1:  # 알파벳 리스트의 숫자가 -1일 때만
                alphaList[i] = j

for i in alphaList:
    print(i,end=' ')
