#https://www.acmicpc.net/problem/16137
#https://www.acmicpc.net/source/75738843

from collections import deque

n,m = map(int,input().split())

ground = []

for _ in range(n):
    ground.append(list(map(int,input().split())))

def solution(graph,visited):
    queue = deque([(0,0,0)])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[0][0][0] = 0
    while queue:
        vx,vy,use_bird_bridge = queue.popleft()
        wait_bridge = False
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or (graph[nx][ny] != 1 and graph[vx][vy] != 1):
                continue
            if graph[nx][ny] == 1:
                if visited[nx][ny][use_bird_bridge] > visited[vx][vy][use_bird_bridge] + 1:
                    visited[nx][ny][use_bird_bridge] = visited[vx][vy][use_bird_bridge] + 1
                    queue.append((nx,ny,use_bird_bridge))
            elif graph[nx][ny] == 0:
                if use_bird_bridge == 1:
                    continue
                if visited[nx][ny][1] > visited[vx][vy][0] + 1:
                    if (visited[vx][vy][0] + 1) % m == 0:
                        visited[nx][ny][1] = visited[vx][vy][0] + 1
                        queue.append((nx,ny,1))
                    else:
                        wait_bridge = True
            else:
                if visited[nx][ny][use_bird_bridge] > visited[vx][vy][use_bird_bridge] + 1:
                    if (visited[vx][vy][use_bird_bridge]+1) % graph[nx][ny] == 0:
                        visited[nx][ny][use_bird_bridge] = visited[vx][vy][use_bird_bridge] + 1
                        queue.append((nx,ny,use_bird_bridge))
                    else:
                        wait_bridge = True
        if wait_bridge == True:
            if vx == n-1 and vy == n-1:
                continue
            visited[vx][vy][use_bird_bridge] += 1
            queue.append((vx,vy,use_bird_bridge))

INF = int(1e9)

visited = [[[INF]*2 for _ in range(n)]for _ in range(n)]
solution(ground,visited)

answer = min(visited[n-1][n-1])
print(answer)
