#https://www.acmicpc.net/problem/23286
#https://www.acmicpc.net/source/73503914

import sys,heapq

input = sys.stdin.readline

n,m,t = map(int,input().split())

graph = [[]for _ in range(n+1)]

for _ in range(m):
    u,v,h = map(int,input().split())
    graph[u].append((v,h))

INF = int(1e9)

max_high = [[INF]*(n+1) for _ in range(n+1)]

def solution(graph,max_high,start):#다익스트라
    q = []
    max_high[start][start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > max_high[start][now]:
            continue
        for next_node, next_hurdle in graph[now]:
            next_highest = max(next_hurdle,max_high[start][now])
            if max_high[start][next_node] > next_highest:
                max_high[start][next_node] = next_highest
                heapq.heappush(q,(next_highest,next_node))

for _ in range(t):
    s,e = map(int,input().split())
    if max_high[s][s] == INF: #정점s에서 나머지 정점까지의 가장 높이가 높은 허들을 탐색 안했을 경우
        solution(graph,max_high,s) #정점s에서 정점e뿐만 아니라 나머지 정점까지의 가장 높이가 높은 허들을 탐색
    answer = max_high[s][e]
    if answer == INF:
        answer = -1
    print(answer)
