#https://www.acmicpc.net/problem/20056
#https://www.acmicpc.net/source/78076708

import sys

input = sys.stdin.readline

def main():
    fire_ball_list = move_fire_ball()
    answer = get_answer(fire_ball_list)
    print(answer)

def move_fire_ball():
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]
    fire_ball_list = create_fire_ball_list()
    for _ in range(k):
        fire_ball_cnt = [[0]*n for _ in range(n)]
        weight = [[0]*n for _ in range(n)]
        direction = [[[0]*3 for _ in range(n)] for _ in range(n)]
        speed = [[0]*n for _ in range(n)]
        for fire_ball in fire_ball_list:
            vx,vy,mi,si,di = fire_ball
            nx = (vx + dx[di] * si) % n
            ny = (vy + dy[di] * si) % n
            fire_ball_cnt[nx][ny] += 1
            weight[nx][ny] += mi
            speed[nx][ny] += si
            direction[nx][ny][2] = di
            direction[nx][ny][di%2] = 1
        fire_ball_list = divide_fire_ball(fire_ball_cnt,weight,speed,direction)
    return fire_ball_list

def create_fire_ball_list():
    fire_ball_list = []
    for _ in range(m):
        r,c,mi,s,d = map(int,input().split())
        fire_ball_list.append((r-1,c-1,mi,s,d))
    return fire_ball_list

def divide_fire_ball(fire_ball_cnt,weight,speed,direction):
    fire_ball_list = []
    for i in range(n):
        for j in range(n):
            if fire_ball_cnt[i][j] == 1:
                fire_ball_list.append((i,j,weight[i][j],speed[i][j],direction[i][j][2]))
                continue
            if weight[i][j] < 5: continue
            nmi = weight[i][j] // 5
            nsi = speed[i][j] // fire_ball_cnt[i][j]
            plus = sum(direction[i][j][:2]) - 1
            for t in range(4):
                fire_ball_list.append((i,j,nmi,nsi,t*2+plus))
    return fire_ball_list

def get_answer(fire_ball_list):
    answer = 0
    for fire_ball in fire_ball_list:
        answer += fire_ball[2]
    return answer

if __name__ == "__main__":
    n,m,k = map(int,input().split())
    main()
