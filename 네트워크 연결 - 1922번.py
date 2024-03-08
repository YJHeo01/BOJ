#https://www.acmicpc.net/problem/1922
#https://www.acmicpc.net/source/74604090

import sys

input = sys.stdin.readline

n = int(input())

parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i

m = int(input())

edges = []

for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

edges.sort()

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

answer = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        answer += cost
        union_parent(parent,a,b)

print(answer)
