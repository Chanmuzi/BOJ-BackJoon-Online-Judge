import sys

a,b,c = map(int,sys.stdin.readline().split())

if b >= c: print(-1)    # 한 대당 추가 비용이 수입보다 크거나 같다면
else:
    print((a//(c-b))+1) # {a를 (b-c)로 나눈 몫 + 1} 만큼 판매하면 됨