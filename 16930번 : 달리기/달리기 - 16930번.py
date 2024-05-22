#https://www.acmicpc.net/problem/16930
#https://www.acmicpc.net/source/78683905

from collections import deque
import sys

input = sys.stdin.readline

def main():
    graph = get_graph(n)
    start_x, start_y, end_x, end_y = map(int,input().split())
    time = [[INF]*m for _ in range(n)]
    direction = [[[False]*4 for _ in range(m)]for _ in range(n)]
    start = (start_x-1,start_y-1)
    bfs(graph,time,direction,start)
    answer = time[end_x-1][end_y-1]
    if answer >= INF: answer = -1
    print(answer)

def get_graph(n):
    graph = []
    for _ in range(n): graph.append(list(input()))
    return graph

def bfs(graph,visited,direction,start):
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            if direction[vx][vy][i] == True:continue
            x, y = vx,vy
            for _ in range(k):
                x += dx[i]; y += dy[i]
                if impossible_move(graph,x,y) or visited[x][y] < visited[vx][vy] + 1: break
                direction[x][y][i] = True; direction[x][y][(i+2)%4] = True
                if visited[x][y] == visited[vx][vy] + 1: continue
                visited[x][y] = visited[vx][vy] + 1
                queue.append((x,y))
            if impossible_move(graph,x,y) == False: direction[x][y][i] = False

def impossible_move(graph,x,y):
    if x < 0 or y < 0 or x >= n or y >= m or graph[x][y] == '#':return True
    return False

if __name__ == "__main__":
    n,m,k = map(int,input().split())
    INF = int(1e9)
    main()
