#https://www.acmicpc.net/problem/1992
#python3으로 제출하면 시간 초과가 되고, PyPy3으로 제출해야 정상적으로 통과 가능합니다.

import sys

input = sys.stdin.readline

INF = int(1e9)
v, e =map(int,input().split())

town = [[INF] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    town[a][b] = c

for i in range(1,v+1):
    for j in range(1,v+1):
        for k in range(1,v+1):
            town[j][k] = min(town[j][k],town[j][i]+town[i][k]) # 플루이드 

answer = INF

for i in range(1,v+1):
    answer = min(answer,town[i][i]) # 사이클은 시작점으로 되돌아올 수 있는 그래프

if answer == INF:
    answer = -1 #자기 자신으로 돌아갈 수 있는 마을이 없으므로 운동 경로 찾기 불가능

print(answer)
