# n,m 입력
n,m = map(int,input().split())

# 수열 리스트 초기화 
sequence = []
 
# 완전 탐색 재귀 함수 
def dfs():
    # 리스트의 요소가 m개면
    if len(sequence)==m:
        # 그 리스트를 문자열로 출력
        print(' '.join(map(str,sequence)))
        # 해당 재귀 함수 종료
        return
    
    # 1부터 n까지
    for i in range(1,n+1):
        # 수열 리스트에 없는 요소를
        if i not in sequence:
            # 수열 리스트에 추가
            sequence.append(i)
            # 재귀 함수 실행
            dfs()
            # 재귀 함수 이후 맨 오른쪽 요소 버리기
            sequence.pop()

# 재귀 함수 실행 
dfs()