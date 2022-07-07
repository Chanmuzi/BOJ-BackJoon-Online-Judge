import sys
sys.setrecursionlimit(10**6)    # 재귀 최대 깊이 설정

def star(x):
    if x == 1:  # 입력값이 1이 되면 재귀 중단
        return ['*']    # 제일 작은 단위인 *

    smaller_star = star(x//3)
    my_list = []
    
    for i in smaller_star:  # 이전 단계에서 함수로 생성된 리스트에 대해
        my_list.append(i*3) 
    for i in smaller_star:
        my_list.append(i + ' '*(x//3) + i)  # x//3 만큼의 공백도 포함
    for i in smaller_star:
        my_list.append(i*3)
    
    return my_list


n = int(sys.stdin.readline())   # 정수 n 입력
print('\n'.join(star(n)))   # 리스트 요소들을 '줄바꿈문자'로 합침