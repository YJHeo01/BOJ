#https://www.acmicpc.net/problem/11559
#https://www.acmicpc.net/source/75332315

from collections import deque

field = []

for _ in range(12):
    field.append(list(input()))

def find_same_puyo_cnt(graph,visited,start):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    puyo_type = graph[start[0]][start[1]]
    puyo_cnt = 1
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= 12 or ny >= 6 or visited[nx][ny] == True or graph[nx][ny] != puyo_type:
                continue
            visited[nx][ny] = True
            puyo_cnt += 1
            queue.append((nx,ny))
    return puyo_cnt

def bang_puyo(graph,start):
    queue = deque([start])
    puyo_type = graph[start[0]][start[1]]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        graph[vx][vy] = '.'
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= 12 or ny >= 6:
                continue
            if graph[nx][ny] == puyo_type:
                queue.append((nx,ny))

def puyo_puyo(graph,visited,start):
    same_puyo_cnt = find_same_puyo_cnt(graph,visited,start)
    if same_puyo_cnt >= 4:
        bang_puyo(graph,start)
        return False
    return True

answer = 0
def gravity_puyo(graph,column):
    before_move_row = 11
    after_move_row = 11
    while True:
        if graph[before_move_row][column] != '.':
            graph[after_move_row][column], graph[before_move_row][column] = graph[before_move_row][column],graph[after_move_row][column]
            after_move_row -= 1
        before_move_row -= 1
        if before_move_row < 0:
            break

while True:
    game_over = True
    visited = [[False]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if field[i][j] != '.' and visited[i][j] == False:
                game_over = puyo_puyo(field,visited,(i,j)) and game_over
    if game_over == True:
        break
    answer += 1
    for i in range(6):
        gravity_puyo(field,i)

print(answer)
