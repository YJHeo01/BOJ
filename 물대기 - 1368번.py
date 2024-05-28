#https://www.acmicpc.net/problem/1368
#https://www.acmicpc.net/source/78949798

import sys,heapq

input = sys.stdin.readline

def main():
    visited = [False] * n
    new_cost = get_new_cost(n)
    answer = 0
    adj_matrix = get_adj_matrix(n)
    q = init_q(new_cost)
    while q:
        cost, vx = heapq.heappop(q)
        if visited[vx] == True: continue
        visited[vx] = True
        answer += cost
        for nx in range(n):
            if visited[nx] == True or adj_matrix[vx][nx] >= new_cost[nx]: continue
            heapq.heappush(q,(adj_matrix[vx][nx],nx))
    print(answer)

def get_new_cost(n):
    new_cost = []
    for _ in range(n):
        new_cost.append(int(input()))
    return new_cost

def get_start_idx(new_cost,n):
    ret_value = 0
    for i in range(1,n):
        if new_cost[ret_value] > new_cost[i]:
            ret_value = i
    return ret_value

def get_adj_matrix(n):
    ret_value = []
    for _ in range(n):
        ret_value.append(list(map(int,input().split())))
    return ret_value

def init_q(new_cost):
    q = []
    for i in range(n):
        heapq.heappush(q,(new_cost[i],i))
    return q

if __name__ == "__main__":
    n = int(input())
    main()
