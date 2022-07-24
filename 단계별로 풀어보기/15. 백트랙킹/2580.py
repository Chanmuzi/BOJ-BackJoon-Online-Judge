import sys
graph = []
blank = []

# 스도쿠판 생성
for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 숫자가 입력되지 않은 위치를 x,y 튜플 형태로 추가
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

# 행검사
def checkRow(x, a):
    # 각 열의 고정된 행에 대해서
    for i in range(9):
        # 동일한 값이 존재하면
        if a == graph[x][i]:
            return False
    # 동일한 값이 없다면
    return True

# 열검사
def checkCol(y, a):
    # 각 행의 고정된 열에 대해서
    for i in range(9):
        # 동일한 값이 존재하면
        if a == graph[i][y]:
            return False
    # 동일한 값이 없다면       
    return True

# 3x3 사각형 검사
def checkRect(x, y, a):
    # 3의 배수에 맞춰 인덱스 수정
    nx = x // 3 * 3
    ny = y // 3 * 3
    # 행
    for i in range(3):
        # 열
        for j in range(3):
            # 동일한 값이 존재하면
            if a == graph[nx+i][ny+j]:
                return False
    # 9칸 내에 동일한 값이 없다면
    return True


def dfs(idx):
    # 공백 칸에 대해 작업을 다 수행하면
    if idx == len(blank):
        # 스도쿠판을 출력
        for i in range(9):
            print(*graph[i])
        # 함수를 종료
        exit(0)

    # 1부터 9까지
    for i in range(1, 10):
        # 공백점들에 대한 좌표 받아오기
        x = blank[idx][0]
        y = blank[idx][1]

        # 행,열,사각형 검사를 통과하면
        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            # 공백점을 i로 변경
            graph[x][y] = i
            # 다음 공백점에 대해 재귀 함수 실행
            dfs(idx+1)
            # 다음 반복을 위한 초기화
            graph[x][y] = 0

dfs(0)