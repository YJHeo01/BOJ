#https://www.acmicpc.net/problem/1119
#https://www.acmicpc.net/source/73708884

adj_matrix = []
n = int(input())
road_cnt = 0
not_have_road_city = [True] * n
for i in range(n):
    tmp = list(input())
    for j in range(i+1,n):
        if tmp[j] == 'Y':
            road_cnt += 1
            not_have_road_city[i] = False
            not_have_road_city[j] = False
    adj_matrix.append(tmp)

def dfs(graph,visited,start):#연결되어 있는 도시들 체크
    for next_idx in range(n):
        if graph[start][next_idx] == 'Y' and visited[next_idx] == False:
            visited[next_idx] = True
            dfs(graph,visited,next_idx)
    return 

for i in not_have_road_city:
    if i == True:
        road_cnt = 0
        break
 
if road_cnt < n-1:#도로가 모든 도시를 연결할 수 없는 상황
    print(-1)
else:
    tmp = 0
    answer = -1
    visited = [False] * (n+1)
    for i in range(n):
        if visited[i] == True:
            continue
        visited[i] = True
        dfs(adj_matrix,visited,i)
        answer += 1
    print(answer)
