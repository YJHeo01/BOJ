#https://www.acmicpc.net/problem/1854
#https://www.acmicpc.net/source/76561884

import sys,heapq

input = sys.stdin.readline

n,m,k = map(int,input().split())

INF = int(1e9)

graph = [[] for _ in range(n+1)]

distance = [[INF]*k for _ in range(n+1)]


for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
k -= 1
def solution(graph,distance):
    q = []
    heapq.heappush(q,(0,1))
    distance[1][0] = 0
    while q:
        vt, vx = heapq.heappop(q)
        if vt > distance[vx][k]:
            continue
        for nx, dt in graph[vx]:
            nt = vt + dt
            if distance[nx][k] > nt:
                distance[nx][k] = nt
                distance[nx].sort()
                heapq.heappush(q,(nt,nx))
                
solution(graph,distance)

for i in range(1,n+1):
    time = distance[i][k]
    if time >= INF:
        time = -1
    print(time)
