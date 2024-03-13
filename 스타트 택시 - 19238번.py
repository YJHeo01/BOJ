#https://www.acmicpc.net/problem/19238
#https://www.acmicpc.net/source/74894031

from collections import deque
import sys

INF = int(1e9)

input = sys.stdin.readline

n,m,energy = map(int,input().split())

customer = [[[]] * n for _ in range(n)]

city = []

for _ in range(n):
    city.append(list(map(int,input().split())))

driver = list(map(int,input().split()))
driver[0] -= 1; driver[1] -= 1
driver.append(energy)

for _ in range(m):
    start_x, start_y, end_x, end_y = map(int,input().split())
    start_x -= 1; start_y -= 1; end_x -= 1; end_y -= 1
    customer[start_x][start_y]=[end_x,end_y]

def find_next_customer(city,customer,distance,driver):
    x,y = driver
    distance[x][y] = 0
    if customer[x][y] != []:
        return (x,y)
    queue = deque([driver])
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    min_distance = INF
    ret_value = (-1,-1)
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or city[nx][ny] == 1:
                continue
            if distance[nx][ny] > distance[vx][vy] + 1:
                distance[nx][ny] = distance[vx][vy] + 1
                if customer[nx][ny] == []:
                    queue.append((nx,ny))
                else:
                    if min_distance > distance[nx][ny]:
                        min_distance = distance[nx][ny]
                        ret_value = (nx,ny)
                    elif min_distance < distance[nx][ny]:
                        return ret_value
                    else:
                        if nx < ret_value[0] or (nx == ret_value[0] and ny < ret_value[1]):
                            ret_value = (nx,ny)

    return ret_value
                    
def move_customer(city,distance,start):
    queue = deque([start])
    distance[start[0]][start[1]] = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]
            if nx < 0 or ny < 0 or ny >= n or nx >= n or city[nx][ny] == 1:
                continue
            if distance[nx][ny] > distance[vx][vy] + 1:
                distance[nx][ny] = distance[vx][vy] + 1
                queue.append((nx,ny))

def solution(city,customer,driver):
    complete_cnt = 0
    driver_x, driver_y, energy = driver
    while True:
        if complete_cnt == m:
            break
        distance = [[INF]*n for _ in range(n)]
        next_customer_x, next_customer_y = find_next_customer(city,customer,distance,(driver_x,driver_y))
        if next_customer_x == -1:
            return -1
        if distance[next_customer_x][next_customer_y] > energy:
            energy = -1
            break
        else:
            energy -= distance[next_customer_x][next_customer_y]
        distance = [[INF]*n for _ in range(n)]
        dest_x, dest_y = customer[next_customer_x][next_customer_y]
        move_customer(city,distance,(next_customer_x,next_customer_y))
        need_energy = distance[dest_x][dest_y]
        if need_energy > energy:
            energy = -1
            break
        else:
            energy += need_energy
            driver_x, driver_y = customer[next_customer_x][next_customer_y]
            customer[next_customer_x][next_customer_y] = []
            complete_cnt += 1
    return energy

print(solution(city,customer,driver))
