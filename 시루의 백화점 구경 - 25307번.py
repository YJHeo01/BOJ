#https://www.acmicpc.net/problem/25307
#https://www.acmicpc.net/source/86375678
#단순 BFS 문제
#요즘 BFS에 대한 감이 떨어졌는지, 마네킹 거리를 구하는 BFS를 실행할 때 마네킹의 위치를 한꺼번에 큐에 넣지 않고, 각각 BFS를 돌려주는 코드를 짜서 TLE 판정을 받았었다.
from collections import deque
import sys

input = sys.stdin.readline

def main():
    graph = [list(map(int,input().split())) for _ in range(n)]
    start = get_start(graph)
    target = get_target(graph)
    dummy_distance = get_dummy_distance(graph)
    distance = [[INF]*m for _ in range(n)]
    get_shortest_path(graph,distance,dummy_distance,start)
    answer = INF
    for x,y in target:
        answer = min(answer,distance[x][y])
    if answer >= INF: answer = -1
    print(answer)

def get_start(graph):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 4: return (i,j)

def get_target(graph):
    ret_value = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                ret_value.append((i,j))
    return ret_value

def get_dummy_distance(graph):
    start = get_dummy(graph)
    ret_value = [[INF]*m for _ in range(n)]
    for x,y in start: ret_value[x][y] = 0
    queue = deque(start)
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if ret_value[nx][ny] > ret_value[vx][vy] + 1:
                ret_value[nx][ny] = ret_value[vx][vy] + 1
                queue.append((nx,ny))
    return ret_value

def get_dummy(graph):
    ret_value = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 3:
                ret_value.append((i,j))
    return ret_value

def get_shortest_path(graph,distance,dummy_distance,start):
    queue = deque([start])
    distance[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or dummy_distance[nx][ny] <= k: continue
            if graph[nx][ny] != 1 and distance[nx][ny] > distance[vx][vy] + 1:
                distance[nx][ny] = distance[vx][vy] + 1
                queue.append((nx,ny))

if __name__ == "__main__":
    INF = int(1e9)
    n,m,k = map(int,input().split())
    main()
