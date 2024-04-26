#https://www.acmicpc.net/problem/22870
#https://www.acmicpc.net/source/77486307

import sys, heapq

input = sys.stdin.readline

INF = int(1e9)

def main():
    global n,m,s,e
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    for i in range(1,n+1):
        graph[i].sort()
    s,e = map(int,input().split())
    distance = [INF] * (n+1)
    dijkstra_start(graph,distance,e)
    answer = distance[s]
    shortest_path = search_shortest_path(graph,distance,[s])
    shortest_path.pop()
    distance = [INF] * (n+1)
    dijkstra_return(graph,distance,shortest_path,e)
    answer += distance[s]
    print(answer)    

def dijkstra_start(graph,distance,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]:
            continue
        for nx, length in graph[vx]:
            if distance[nx] > dist + length:
                distance[nx] = dist + length
                heapq.heappush(q,(distance[nx],nx))

def search_shortest_path(graph,distance,path):
    vx = path[0]
    if vx == e:
        return path
    for nx, length in graph[vx]:
        if distance[nx] + length == distance[vx]:
            return search_shortest_path(graph,distance,[nx]+path)

def dijkstra_return(graph,distance,prohabit_node,start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, vx = heapq.heappop(q)
        if dist > distance[vx]:
            continue
        for nx, length in graph[vx]:
            if nx in prohabit_node:
                continue
            if distance[nx] > dist + length:
                distance[nx] = dist + length
                heapq.heappush(q,(distance[nx],nx))

if __name__ == "__main__":
    main()
