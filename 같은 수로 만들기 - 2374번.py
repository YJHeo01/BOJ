#https://www.acmicpc.net/problem/2374
#https://www.acmicpc.net/source/86833548
#알고리즘 : 그리디 알고리즘, 유니온 파인드
#Add 연산을 사용할 때 커지는 값이 가장 작은 순서대로 add 연산 횟수를 구함
#각 그룹의 좌측, 우측 경계를 기록하기 위해 유니온 파인드 사용

import sys, heapq

input = sys.stdin.readline

n = int(input())

array = [int(input()) for _ in range(n)]

q = []

parent_right = list(range(n)) #우측 경계 기록
parent_left = list(range(n)) #좌측 경계 기록

for i in range(1,n):
    heapq.heappush(q,(max(array[i],array[i-1]),-min(array[i],array[i-1]),i-1,i))

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent_left(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def union_parent_right(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

answer = 0

while q:
    max_value, min_value, l, r = heapq.heappop(q) #Add 연산을 사용할 때 커지는 값이 가장 작은 순서대로 add 연산 횟수를 구함
    if find_parent(parent_right,l) == find_parent(parent_right,r): continue
    min_value *= -1
    union_parent_left(parent_left,l,r)
    union_parent_right(parent_right,l,r)
    answer += (max_value-min_value)
    l_side, r_side = find_parent(parent_left,l), find_parent(parent_right,r)
    array[l_side], array[r_side] = max_value, max_value
    if l_side != 0:
        left_value = array[l_side-1]
        left_max_value, left_min_value = max(left_value,max_value), min(left_value,max_value)
        heapq.heappush(q,(left_max_value,-left_min_value,l_side-1,l_side))
    if r_side != n - 1:
        right_value = array[r_side+1]
        right_max_value, right_min_value = max(right_value,max_value), min(right_value,max_value)
        heapq.heappush(q,(right_max_value,-right_min_value,r_side,r_side+1))

print(answer)
