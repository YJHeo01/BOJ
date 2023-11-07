from collections import deque

m,n,k = map(int,input().split())

def bfs(graph,visited,start):
    queue = deque([start])
    ret_v = 1
    visited[start[0]][start[1]] = 1
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    while queue:
        vy, vx = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[ny][nx] == 0 and graph[ny][nx] == 0:
                queue.append((ny,nx))
                visited[ny][nx] = 1
                ret_v += 1
    return ret_v

answer = []

graph = [[0]*(n) for _ in range(m)]

visited = [[0]*(n) for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = 1 #눈금이 존재하는 직사각형


cnt = 0 # 분리된 영역의 개수
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and visited[i][j] == 0: #눈금이 존재하지 않고, 탐색하지 않은 새로운 영역
            tmp = bfs(graph,visited,(i,j))
            answer.append(tmp)
            cnt += 1

answer.sort()
print(cnt)
for i in answer:
    print(i,end = ' ')
