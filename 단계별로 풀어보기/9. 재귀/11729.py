# 원판 개수
n = int(input())
count = 0

def hanoi(x,start,help,end):  # 원판 개수, 시작, 중간, 목표 기둥
    global count    # 이동 횟수, print 직후에만 count
    if x == 1:  # 마지막 원판
        print(start,end) # 시작 -> 목표
        count += 1
        return count
    
    
    hanoi(x-1,start,end,help)   # x-1개를 중간 기둥에 전부 보냄
    print(start,end)    
    count += 1
    
    hanoi(x-1,help,start,end)   # x-1개를 중간 -> 목표 기둥에 보냄
    return count

print(hanoi(n,1,2,3)) # n개 원판을 1번에서 2번을 거쳐 3번 기둥으로

sum = 0
for i in range(n):
    sum += (1 + sum)  
    # n-1개의 원판을 중간 기둥에 모두 보냈으므로 (남은 1개를 목표로
    # 보내는 데) 1번 + (중간기둥->목표기둥) sum번 합산
print(sum)