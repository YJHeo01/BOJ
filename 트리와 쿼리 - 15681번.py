#https://www.acmicpc.net/problem/15681
#https://www.acmicpc.net/source/79453901

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    n,r,q = map(int,input().split())
    tree = get_tree(n)
    cnt = [0] * (n+1)
    dfs(tree,cnt,r)
    for _ in range(q):
        u = int(input())
        print(cnt[u])

def get_tree(n):
    tree = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)
    return tree

def dfs(graph,cnt,vx):
    cnt[vx] = 1
    for nx in graph[vx]:
        if cnt[nx] != 0: continue
        cnt[vx] += dfs(graph,cnt,nx)
    return cnt[vx]

if __name__ == "__main__":
    main()
