#https://www.acmicpc.net/problem/1005
#https://www.acmicpc.net/source/71154349
#https://github.com/YJHeo01
#pypy3

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

INF = int(1e9)

def dfs(building,visited):
    return_set = set([])
    if reverse_tech_tree[building] == []:
        return set([building])
    for i in reverse_tech_tree[building]:
        if visited[i] == False:
            visited[i] = True
            return_set = return_set | dfs(i,visited)
    return return_set

    
def search_start_build(building,visited):
    return dfs(building,visited)

def bfs(graph,visited,start,time):
    queue = deque(list(start))
    while queue:
        building = queue.popleft()
        for next_building in graph[building]:
            if visited[next_building] < visited[building] + time[next_building]:
                visited[next_building] = visited[building] + time[next_building]
                queue.append(next_building)

def search_answer(tech_tree,time_list,start,time):
    bfs(tech_tree,time_list,start,time)

for _ in range(t):
    n,k = map(int,input().split())
    build_time = [0] + list(map(int,input().split()))
    tech_tree = [[] for _ in range(n+1)]
    reverse_tech_tree = [[] for _ in range(n+1)]
    for _ in range(k):
        pre_building, building = map(int,input().split())
        tech_tree[pre_building].append(building)
        reverse_tech_tree[building].append(pre_building)
    destination_building = int(input())
    visited = [False] * (n+1)
    start_build = search_start_build(destination_building,visited)
    dp = [0] * (n+1)
    for build in start_build:
        dp[build] = build_time[build]
    search_answer(tech_tree,dp,start_build,build_time)
    print(dp[destination_building])
