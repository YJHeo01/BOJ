from collections import deque

n,m = map(int,input().split())
jump = [0] * 101 # 뱀, 사다리의 정보를 저장, 0으로 초기화를 해줬으니 0이 아닌 경우 그 좌표에는 뱀 혹은 사다리가 존재
for i in range(n+m):
    x,y = map(int,input().split())
    jump[x] = y # 뱀, 사다리 모두 위치를 워프하므로 같이 저장해준다.

visited = [0] * 101 # 좌표별로 주사위를 몇번 굴렸는지 저장하는 리스트

def bfs(visited,jump,start):
    queue = deque([start])
    visited[1] = 0 #시작점이니 주사위를 안굴려도 위치함
    while queue:
        vx = queue.popleft()
        for i in range(6,0,-1): 
            nx = vx + i 
            if nx > 100:
                continue #100이 넘는 점은 갈 수 없다.
            if jump[nx] != 0: #뱀 또는 사다리 존재
                nx = jump[nx] 
            if visited[nx] == 0 or visited[nx] > visited[vx] + 1:
                queue.append(nx)
                visited[nx] = visited[vx] + 1
bfs(visited,jump,1)

print(visited[100])
