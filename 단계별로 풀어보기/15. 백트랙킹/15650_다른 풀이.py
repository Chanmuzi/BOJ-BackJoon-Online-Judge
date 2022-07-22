# n,m 입력 받기
n,m = map(int,input().split())
# 조합 리스트 초기화
arr = []

def dfs(start):
    # 리스트의 길이가 꽉 차면
    if len(arr) == m:
        # 모든 요소를 문자열로 묶어 출력 하고
        print(' '.join(map(str,arr)))
        # 재귀 함수 종료
        return
    
    for i in range(start,n+1):
        # 리스트에 없는 요소만 추가
        if i not in arr:
            arr.append(i)
            # 시작점을 높여서 재귀 함수 실행
            dfs(i+1)
            # 마지막 요소 제거
            arr.pop()

dfs(1)