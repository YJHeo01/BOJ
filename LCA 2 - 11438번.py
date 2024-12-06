#https://www.acmicpc.net/problem/11438
#https://www.acmicpc.net/source/87221640

import sys

sys.setrecursionlimit(int(1e5)+10)
input = sys.stdin.readline

def main():
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        graph[a].append(b); graph[b].append(a)
    parent = [[0]*(20) for _ in range(n+1)]
    depth = [-1] * (n+1)
    depth[1] = 0
    dfs(graph,depth,parent,1)
    set_parent(parent)
    
    m = int(input())
    for _ in range(m):
        a,b = map(int,input().split())
        print(solution(parent,depth,a,b))

def dfs(graph,depth,parent,vx):
    for nx in graph[vx]:
        if depth[nx] != -1: continue
        depth[nx] = depth[vx] + 1
        parent[nx][0] = vx
        dfs(graph,depth,parent,nx)

def set_parent(parent):
    for i in range(1,20):
        for j in range(n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def solution(parent,depth,a,b):
    if depth[a] > depth[b]: a,b = b,a
    tmp = 1 << 19
    for i in range(19,-1,-1):
        if depth[b] - depth[a] >= tmp:
            b = parent[b][i]
        tmp >>= 1
    if a == b: return a
    for i in range(19,-1,-1):
        if parent[a][i] != parent[b][i]:
            a,b = parent[a][i], parent[b][i]
    return parent[a][0]

if __name__ == "__main__":
    n = int(input())
    main()
