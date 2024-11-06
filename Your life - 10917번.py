#https://www.acmicpc.net/problem/10917
#https://www.acmicpc.net/source/86088841
#그래프 이론, BFS를 활용하여 해결하는 문제
#상황이 정점, 변화가 간선인 그래프로 생각하면, 무난하게 해결 가능한 BFS 문제이다.
#2024-11-06 기준 Solved.ac 난이도 S2

from collections import deque
import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        x,y = map(int,input().split())
        graph[x].append(y)
    visited = [-1] * (n+1)
    bfs(graph,visited)
    print(visited[n])

def bfs(graph,visited):
    queue = deque([1])
    visited[1] = 0
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if visited[nx] == -1:
                visited[nx] = visited[vx] + 1
                queue.append(nx)

if __name__ == "__main__":
    main()
