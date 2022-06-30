numbers = set(range(1,10001))
removeSet = set()

for number in numbers:
    for n in str(number):   # 문자형으로 바꾸어 순서를 만들고 각 문자를 정수로 바꾸면서 더한다
        number += int(n)
    if number <= 10000:
        removeSet.add(number)   # 10000이 넘지 않으면 제거set에 추가

selfNums = numbers - removeSet  # 차집합
for selfNum in sorted(selfNums):# 리스트 정렬
    print(selfNum)