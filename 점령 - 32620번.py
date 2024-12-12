#https://www.acmicpc.net/problem/32620
#https://www.acmicpc.net/source/87392442
#다익스트라

import sys, heapq

input = sys.stdin.readline

def main():
    n,m,r = map(int,input().split())
    a = [0] + list(map(int,input().split()))
    b = [0] + list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v); graph[v].append(u)
    answer = solution(graph,a,b,[False]*(n+1),r)
    print(answer)

def solution(graph,a,b,visited,start):
    q = []
    ret_value = 0
    visited[start] = True
    heapq.heappush(q,(0,start))
    while q:
        need_power, vx = heapq.heappop(q) #필요한 기력이 적은 순서대로 방문
        if need_power > ret_value: break
        ret_value += b[vx]
        for nx in graph[vx]:
            if visited[nx] == False: #이미 우선순위 큐에 넣은 경우, 큐에 넣지 않도록
                visited[nx] = True
                heapq.heappush(q,(a[nx],nx))
    return ret_value

if __name__ == "__main__":
    main()
