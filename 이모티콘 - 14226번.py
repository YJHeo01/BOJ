#https://www.acmicpc.net/problem/14226
#https://www.acmicpc.net/source/75656799

from collections import deque

s = int(input())

INF = int(1e9)

visited = [INF] * (2 *(s+1))

def solution(visited):
    queue = deque([1])
    visited[1] = 0
    while queue:
        vx = queue.popleft()
        nx = vx - 1
        if nx >= 0 and visited[nx] > visited[vx] + 1:
            visited[nx] = visited[vx] + 1
            queue.append(nx)
        for i in range(2,2001):
            nx = vx * i
            if nx > 2*s:
                break
            if visited[nx] > visited[vx] + i:
                visited[nx] = visited[vx] + i
                queue.append(nx)

solution(visited)

answer = visited[s]

print(answer)
