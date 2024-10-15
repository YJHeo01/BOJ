#https://www.acmicpc.net/problem/13308
#https://www.acmicpc.net/source/85225211

import heapq, sys

input = sys.stdin.readline

def main():
    gas_station = [0] + list(map(int,input().split()))
    distance = [[INF]*2501 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    print(dijkstra(graph,distance,gas_station))
    
def dijkstra(graph,distance,gas_station):
    distance[1][2500] = 0
    q = []
    ret_value = INF
    heapq.heappush(q,(0,2500,1))
    while q:
        dist, min_price, vx = heapq.heappop(q)
        if dist > min(distance[vx][min_price],ret_value): continue
        if vx == n:
            ret_value = min(ret_value,dist)
            continue
        min_price = min(min_price,gas_station[vx])
        for nx, length in graph[vx]:
            new_min_price = min(min_price,gas_station[nx])
            if distance[nx][new_min_price] > dist + min_price * length:
                distance[nx][new_min_price] = dist + min_price * length
                heapq.heappush(q,(distance[nx][new_min_price],new_min_price,nx))
    return ret_value

if __name__ == "__main__":
    INF = 2500 ** 3
    n,m = map(int,input().split())
    main()
