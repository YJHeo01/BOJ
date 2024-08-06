#https://www.acmicpc.net/problem/16564
#https://www.acmicpc.net/source/82109689

import sys

input = sys.stdin.readline

n,k = map(int,input().split())
level = sorted([int(input()) for _ in range(n)])
answer = level[0]
cnt = n

for i in range(1,n):
    if k >= (level[i] - level[i-1]) * i:
        k -= (level[i] - level[i-1]) * i
        answer = level[i]
    else:
        cnt = i
        break

if k != 0:
    answer += k // cnt

print(answer)
