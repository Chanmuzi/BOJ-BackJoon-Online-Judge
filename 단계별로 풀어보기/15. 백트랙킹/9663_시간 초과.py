# n 입력 받기
n = int(input())

# 경우의 수 초기화
ans = 0
# 각 줄의 퀸의 위치
row = [0] * n

# x번 인덱스 줄에 대해 검사
def is_promising(x):
    # 0번 인덱스부터 x 이전까지, 즉 윗줄에 대해서 검사
    for i in range(x):
        # 같은 열에 위치하거나 or 대각선에 위치하는 경우 False를 return
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    # 같은 열에 위치하지도, 대각선에 위치하지도 않을 때는 True를 반환
    return True

def n_queens(x):
    # 전역 변수 불러오기
    global ans
    # x가 n이 되면
    if x == n:
        # 경우의 수 추가 후 종료
        ans += 1
        return

    else:
        # n줄에 대해 반복
        for i in range(n):
            # [x, i]에 퀸 놓기
            row[x] = i
            # is_promising 함수가 True로 return 될 때
            if is_promising(x):
                # 다음 줄에 퀸 놓기
                n_queens(x+1)

# x=0부터 시작
n_queens(0)
# 총 경우의 수 출력
print(ans)