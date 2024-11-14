#https://www.acmicpc.net/problem/28069
#https://www.acmicpc.net/source/86429183
#0번째 계단에서 제자리걸음이 가능하므로, 최적의 경우 k번 이하로 N번째 계단에 도달할 경우, 무조건 k번째 행동에서 N번째 계단으로 도착 가능
from collections import deque

n,k = map(int,input().split())
visited = [k+1] * (n+1)

def bfs(visited):
    queue = deque([0])
    visited[0] = 0
    while queue:
        vx = queue.popleft()
        for dx in [1,vx//2]:
            nx = vx + dx
            if nx > n or visited[nx] <= visited[vx] + 1: continue
            visited[nx] = visited[vx] + 1
            queue.append(nx)
bfs(visited)

if visited[n] > k:
    print("water")
else:
    print("minigimbob")
