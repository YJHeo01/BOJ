#https://www.acmicpc.net/problem/20056
#https://www.acmicpc.net/source/75632115

import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

fire_ball_list = []

fire_ball_cnt = [[0]*n for _ in range(n)]

weight = [[0]*n for _ in range(n)]
direction = [[0]*n for _ in range(n)]
speed = [[0]*n for _ in range(n)]

for _ in range(m):
    r,c,mi,s,d = map(int,input().split())
    fire_ball_list.append((r-1,c-1,mi,s,d))

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

while True:
    if k == 0:
        break
    for i in range(n):
        for j in range(n):
            fire_ball_cnt[i][j] = 0
            weight[i][j] = 0
            speed[i][j] = 0
            direction[i][j] = 0
    k -= 1
    even_num = [[False]*n for _ in range(n)]
    odd_num = [[False]* n for _ in range(n)]
    for fire_ball in fire_ball_list:
        vx,vy,mi,si,di = fire_ball
        nx = (vx + dx[di] * si) % n
        ny = (vy + dy[di] * si) % n
        fire_ball_cnt[nx][ny] += 1
        weight[nx][ny] += mi
        speed[nx][ny] += si
        direction[nx][ny] += di
        if di % 2 == 1:
            odd_num[nx][ny] = True
        else:
            even_num[nx][ny] = True
    fire_ball_list = []

    for i in range(n):
        for j in range(n):
            if fire_ball_cnt[i][j] == 1:
                fire_ball_list.append((i,j,weight[i][j],speed[i][j],direction[i][j]))
            else:
                if weight[i][j] >= 5:
                    nmi = weight[i][j] // 5
                    nsi = speed[i][j] // fire_ball_cnt[i][j]
                    if even_num[i][j] & odd_num[i][j]:
                        plus = 1
                    else:
                        plus = 0
                    for t in range(4):
                        fire_ball_list.append((i,j,nmi,nsi,t*2+plus))
answer = 0

for fire_ball in fire_ball_list:
    answer += fire_ball[2]

print(answer)
