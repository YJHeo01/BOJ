from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

INF = int(1e9)


graph_A = [[] for _ in range(n+1)]
graph_B = [[] for _ in range(n+1)]


for _ in range(m):
    a,b = map(int,input().split())
    graph_A[a].append(b)
    graph_B[b].append(a)

answer = 0

def check_answer(graph,visited,start):
    queue = deque([start])
    check_cnt = 0
    visited[start] = True
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] == False:
                visited[nx] = True
                check_cnt += 1
                queue.append(nx)
    if check_cnt >= ((n//2)+(n%2)):
        return True
    else:
        return False

for i in range(1,n+1):
    visited = [False] * (n+1)
    if check_answer(graph_A,visited,i) == True or check_answer(graph_B,visited,i) == True:
        answer += 1

print(answer)
