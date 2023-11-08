#https://www.acmicpc.net/problem/1197

import sys

input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return
v, e = map(int,input().split())

edges = []

parent = [0] * (v+1)

for i in range(1,v+1):
    parent[i] = i
for _ in range(e):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

edges.sort() #가중치가 작은 순서대로 간선 정렬

result = 0
for edge in edges:
    c,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b): #둘이 같은데 합치면 사이클이 생김
        union_parent(parent,a,b)
        result += c

print(result)
