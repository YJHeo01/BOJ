#https://www.acmicpc.net/problem/1113
#https://www.acmicpc.net/source/77363778

from collections import deque

n,m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(input()))

for i in range(n):
    for j in range(m):
        graph[i][j] = int(graph[i][j])

def possible_build_waterpark(graph,visited,start,height):
    ret_value = True
    queue = deque([start])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[start[0]][start[1]] = True
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                ret_value = False
                continue
            if graph[nx][ny] < height and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx,ny))
    return ret_value

def build_water_park(graph,water_park,start,height):
    queue = deque([start])
    ret_value = 1
    water_park[start[0]][start[1]] = True
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    graph[start[0]][start[1]] += 1
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if height > graph[nx][ny] and water_park[nx][ny] == False:
                ret_value += 1
                water_park[nx][ny] = True
                graph[nx][ny] += 1
                queue.append((nx,ny))
    return ret_value

answer = 0

for height in range(2,10):
    visited = [[False]*m for _ in range(n)]
    water_park = [[False]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if visited[x][y] == True or graph[x][y] >= height:
                continue
            if possible_build_waterpark(graph,visited,(x,y),height) == True:
                answer += build_water_park(graph,water_park,(x,y),height)
    
print(answer)
