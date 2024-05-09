#https://www.acmicpc.net/problem/22116
#https://www.acmicpc.net/source/78098214 : 데이크스트라 내 변수명 visited -> distance

import sys,heapq

input = sys.stdin.readline

INF = int(1e9)

def main():
    board = get_board()
    visited = [[INF]*n for _ in range(n)]
    answer = dijkstra(board,visited)
    print(answer)

def get_board():
    board = []
    for _ in range(n):
        board.append(list(map(int,input().split())))
    return board

def dijkstra(graph,distance):
    q = []
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    distance[0][0] = 0
    heapq.heappush(q,(0,0,0))
    while q:
        vd,vx,vy = heapq.heappop(q)
        if vd > distance[vx][vy]: continue
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if exit_graph(nx,ny): continue
            nd = max(vd,abs(graph[nx][ny] - graph[vx][vy]))
            if distance[nx][ny] > nd:
                distance[nx][ny] = nd
                heapq.heappush(q,(nd,nx,ny))
    return distance[n-1][n-1]

def exit_graph(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return True
    return False

if __name__ == "__main__":
    n = int(input())
    main()
