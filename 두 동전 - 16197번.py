#https://www.acmicpc.net/problem/16197
#https://www.acmicpc.net/source/74599681

from collections import deque

n,m = map(int,input().split())

board = []

coin_list = []

for i in range(n):
    tmp = list(input())
    board.append(tmp)
    for j in range(m):
        if tmp[j] == 'o':
            coin_list.append([i,j])

def solution(graph,start):
    visited = [[[[False]*m for _ in range(n)]for _ in range(m)]for _ in range(n)]
    queue = deque([start+[1]])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        coin_A, coin_B, move_cnt = queue.popleft()
        A_vx, A_vy = coin_A
        B_vx, B_vy = coin_B
        for i in range(4):
            out_coin_cnt = 0
            A_nx = A_vx + dx[i]
            A_ny = A_vy + dy[i]
            if A_nx < 0 or A_ny < 0 or A_nx >= n or A_ny >= m:
                out_coin_cnt += 1
            else:
                if graph[A_nx][A_ny] == '#':
                    A_nx, A_ny = A_vx, A_vy
                coin_A = [A_nx,A_ny]
            B_nx = B_vx + dx[i]
            B_ny = B_vy + dy[i]
            if B_nx < 0 or B_ny < 0 or B_nx >= n or B_ny >= m:
                out_coin_cnt += 1
            else:
                if graph[B_nx][B_ny] == '#':
                    B_nx, B_ny = B_vx, B_vy
                coin_B = [B_nx,B_ny]
            if out_coin_cnt != 0:
                if out_coin_cnt == 1:
                    return move_cnt
                continue
            else:
                if visited[A_nx][A_ny][B_nx][B_ny] == True or move_cnt == 10:
                    continue
                visited[A_nx][A_ny][B_nx][B_ny] = True
                queue.append((coin_A,coin_B,move_cnt+1))
    return -1

answer = solution(board,coin_list)

print(answer)
