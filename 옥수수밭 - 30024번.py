#https://www.acmicpc.net/problem/30024
#https://www.acmicpc.net/source/85533793

import sys, heapq

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    k = int(input())
    q = []
    for i in range(n):
        visited[i][0] = True
        heapq.heappush(q,(-graph[i][0],i,0))
        
    for i in range(n):
        if visited[i][m-1]: break
        visited[i][m-1] = True
        heapq.heappush(q,(-graph[i][m-1],i,m-1))
    
    for i in range(m):
        if visited[0][i]: continue
        visited[0][i] = True
        heapq.heappush(q,(-graph[0][i],0,i))
        
    for i in range(m):
        if visited[n-1][i]: continue
        visited[n-1][i] = True
        heapq.heappush(q,(-graph[n-1][i],n-1,i))
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    for _ in range(k):
        tmp, vx, vy = heapq.heappop(q)
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny]: continue
            visited[nx][ny] = True
            heapq.heappush(q,(-graph[nx][ny],nx,ny))
        print(vx+1,vy+1)

if __name__ == "__main__":
    main()
