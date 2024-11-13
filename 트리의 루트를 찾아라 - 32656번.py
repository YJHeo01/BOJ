#https://www.acmicpc.net/problem/32656
#https://www.acmicpc.net/source/86392830
# a,b,x쌍에서 a,b는 x와 같은 값이 아닌 경우 루트가 될 수 없고, x와 a,b 사이의 노드를 루트 후보에서 제외시킨다. 이때, BFS를 활용한다.
from collections import deque
import sys

input = sys.stdin.readline

def main():
    n = int(input())
    tree = [[] for _ in range(n+1)]
    possible_root = [True] * (n+1)
    for _ in range(n-1):
        a,b = map(int,input().split())
        tree[a].append(b); tree[b].append(a)
    a,b,x = map(int,input().split())
    if a != x: bfs(tree,possible_root,a,x)
    if b != x: bfs(tree,possible_root,b,x)
    answer = 0
    for i in range(1,n+1):
        if possible_root[i]: answer += 1
    print(answer)

def bfs(graph,visited,start,block):
    queue = deque([start])
    visited[start] = False
    while queue:
        vx = queue.popleft()
        for nx in graph[vx]:
            if nx == block or visited[nx] == False: continue
            visited[nx] = False
            queue.append(nx)

if __name__ == "__main__":
    main()
