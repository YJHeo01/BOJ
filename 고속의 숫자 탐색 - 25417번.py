#https://www.acmicpc.net/problem/25417
#https://www.acmicpc.net/source/72620134
from collections import deque

board = []
dest = (-1,-1)
for i in range(5):
    tmp = list(map(int,input().split()))
    board.append(tmp)
    if dest != (-1,-1):
        continue
    for j in range(5):
        if tmp[j] == 1:
            dest = (i,j)
            break

r,c = map(int,input().split())

INF = int(1e9)
move_cnt = [[INF]*5 for _ in range(5)]

def run(graph,direction,start):
    nx,ny = start
    dx,dy = direction
    while True:
        nx += dx
        ny += dy
        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5 or graph[nx][ny] == -1:
            nx -= dx
            ny -= dy
            break
        if graph[nx][ny] == 7:
            break
    return nx,ny

def solution(graph,move_cnt,start):
    queue = deque([start])
    move_cnt[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5 or graph[nx][ny] == -1:
                continue
            if move_cnt[nx][ny] > move_cnt[vx][vy] + 1:
                move_cnt[nx][ny] = move_cnt[vx][vy] + 1
                queue.append((nx,ny))
            if graph[nx][ny] == 7:
                continue
            nx,ny = run(graph,(dx[i],dy[i]),(nx,ny))
            if move_cnt[nx][ny] > move_cnt[vx][vy] + 1:
                move_cnt[nx][ny] = move_cnt[vx][vy] + 1
                queue.append((nx,ny))
solution(board,move_cnt,(r,c))

answer = move_cnt[dest[0]][dest[1]]
if answer == INF:
    answer = -1

print(answer)
