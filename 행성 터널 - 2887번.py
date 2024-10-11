#https://www.acmicpc.net/problem/2887
#https://www.acmicpc.net/source/85062332

import sys, heapq

input = sys.stdin.readline

def main():
    planet_list = []
    n = int(input())
    for i in range(n):
        planet_list.append(list(map(int,input().split()))+[i])
    path_list = []
    for i in range(3):
        planet_list.sort(key=lambda x : x[i])
        for j in range(1,n):
            heapq.heappush(path_list,(planet_list[j][i]-planet_list[j-1][i],planet_list[j][3],planet_list[j-1][3]))
    parent = list(range(n))
    answer = 0
    while path_list:
        dist, x, y = heapq.heappop(path_list)
        if find_parent(parent,x) == find_parent(parent,y):
            continue
        answer += dist
        union_parent(parent,x,y)
    print(answer)

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
