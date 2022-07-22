# n,m 입력 받기
n,m = map(int,input().split())
# 중복 조합 리스트 초기화
arr = []

def dfs():
    # 리스트의 길이가 m일 때
    if len(arr)==m:
        # 리스트 요소 출력
        print(*arr) 
        # 재귀 함수 종료
        return

    # 1부터 n까지
    for i in range(1,n+1):
        # i를 리스트에 추가
        arr.append(i)
        # 재귀 함수 실행
        dfs()
        # 마지막 요소 버리기
        arr.pop()
        
dfs()