import sys
# k 정수로 입력 받기
k = int(sys.stdin.readline())

# 변화 방향과 크기 리스트 초기화
vector_list = []
grade_list = []

# 입력되는 변화 방향과 크기 리스트에 추가
for i in range(6):
    vector,grade = map(int,sys.stdin.readline().split())
    vector_list.append(vector)
    grade_list.append(grade)

# 큰 사각형, 작은 사각형, 총 면적 변수 초기화    
big_square = 0
small_square = 0
total = 0
# 육각형 그린 방식에 따라 사각형 면적 구하기
if vector_list == [4,2,4,2,3,1]:
    big_square = grade_list[4] * grade_list[5]
    small_square = grade_list[1] * grade_list[2]
elif vector_list == [4,2,3,1,3,1]:
    big_square = grade_list[0] * grade_list[1]
    small_square = grade_list[3] * grade_list[4]
elif vector_list == [4,2,3,1,4,1]:
    big_square = grade_list[1] * grade_list[2]
    small_square = grade_list[4] * grade_list[5]
else:
    big_square = grade_list[0] * grade_list[5]
    small_square = grade_list[2] * grade_list[3]

# 전체 면적 = 큰 사각형 - 작은 사각형
total = big_square - small_square
# 면적과 k를 곱해서 출력
print(total * k)