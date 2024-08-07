#https://www.acmicpc.net/problem/13905
#https://www.acmicpc.net/source/81466995

import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    s,e = map(int,input().split())
    parent = [0] * (n+1)
    for i in range(n+1):
        parent[i] = i
    bridges = []
    for _ in range(m):
        bridges.append(list(map(int,input().split())))
    bridges.sort(key= lambda x : -x[2])
    for h1,h2,k in bridges:
        union_parent(parent,h1,h2)
        if find_parent(parent,s) == find_parent(parent,e):
            print(k)
            return
    print(0)

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    main()
