import sys

# n 입력 받기, 공백 리스트 생성
n = int(sys.stdin.readline())
word_list = []

# 입력 받은 단어들을 리스트에 추가 
# rstrip으로 줄바꿈 문자 제거
for i in range(n):
    word_list.append(sys.stdin.readline().rstrip())

# 세트형으로 바꿔 중복 문자 제거 후 리스트로 재변환
word_list = list(set(word_list))
# 알파벳 순으로 정렬
word_list.sort()
# 문자열 길이로 정렬
word_list.sort(key = lambda x: len(x))

# 순서대로 출력
for i in word_list:
    print(i)