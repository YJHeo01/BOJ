#https://www.acmicpc.net/problem/20040

import sys

input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_set(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a == b:
        return 1 # 사이클 발견
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b
    return 0

n,m = map(int,input().split())

parent = [0] * n

for i in range(1,n):
    parent[i] = i
answer = 0
for i in range(m):
    a,b = map(int,input().split())
    answer = union_set(parent,a,b)
    if answer != 0:
        answer += i
        break
print(answer)
