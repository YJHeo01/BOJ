#https://www.acmicpc.net/problem/13141
#https://www.acmicpc.net/source/87326754
#플루이드 워셜

import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    adj_matrix = [[INF]*(n+1) for _ in range(n+1)] #인접 행렬
    for i in range(n+1): adj_matrix[i][i] = 0
    edges = []
    for _ in range(m):
        s,e,l = map(int,input().split())
        edges.append((s,e,l))
        adj_matrix[s][e] = min(l,adj_matrix[s][e])
        adj_matrix[e][s] = min(l,adj_matrix[e][s])
    
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                adj_matrix[i][j] = min(adj_matrix[i][j],adj_matrix[i][k]+adj_matrix[k][j])
    answer = INF
    
    for i in range(1,n+1):#처음에 불을 붙인 노드
        tmp = 0
        for s,e,l in edges:
            start_time, end_time = adj_matrix[i][s], adj_matrix[i][e]
            if start_time > end_time: start_time,end_time = end_time,start_time
            if start_time + l == end_time: #작은 거리 + l = 큰 거리이므로, 양 끝점에 불이 붙지 않음
                tmp = max(tmp,2 * end_time)
            else: #양 끝 정점에 불이 붙음
                tmp = max(tmp,2 * end_time+(l - end_time + start_time))
        answer = min(answer,tmp)
    
    print(answer//2,end=".")
    if answer % 2 == 0:
        print(0)
    else:
        print(5)

if __name__ == "__main__":
    INF = int(1e9)
    main()
