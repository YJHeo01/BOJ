#https://www.acmicpc.net/problem/20057
#https://www.acmicpc.net/source/77757383

import sys

input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def main():
    board = get_board()
    x,y = (n-1)//2, (n-1)//2
    answer, move_length = 0,1
    while True:
        for i in range(4):
            for _ in range(move_length):
                x += dx[i]
                y += dy[i]
                if exit_board(x,y) == True:
                    print(answer)
                    return
                answer += move_wind(board,(x,y),i)
                board[x][y] = 0
            if i % 2 == 1:
                move_length += 1
            
def get_board():
    board = []
    for _ in range(n):
        board.append(list(map(int,input().split())))
    return board

def exit_board(x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return True
    return False

def move_wind(graph,start,direction):
    vx,vy = start; ret_value = 0
    alpha_value = graph[vx][vy]; start_value = alpha_value
    alpha_x = vx + dx[direction]; alpha_y = vy + dy[direction]
    
    if start_value >= 10:
        tmp = start_value // 10
        alpha_value -= 2 * tmp
        ret_value += ten_percent(graph,start,direction)

    if (start_value*7) // 100 != 0:
        tmp = (start_value *7) // 100
        alpha_value -= tmp * 2
        ret_value += seven_percent(graph,start,direction)
    
    if start_value >= 20:
        tmp = start_value // 20
        alpha_value -= tmp
        ret_value += five_percent(graph,start,direction)

    if start_value >= 50:
        tmp = start_value // 50
        alpha_value -= 2 * tmp
        ret_value += two_percent(graph,start,direction)

    if start_value >= 100:
        tmp = start_value // 100
        alpha_value -= 2 * tmp 
        ret_value += one_percent(graph,start,direction)

    if exit_board(alpha_x,alpha_y) == True:
        ret_value += alpha_value
    else:
        graph[alpha_x][alpha_y] += alpha_value
    return ret_value

def ten_percent(graph,start,direction):
    vx,vy = start
    ret_value = 0
    tmp = graph[vx][vy] // 10
    for i in [-1,1]:
        nx = vx + dx[direction] + dx[(direction+i)%4]
        ny = vy + dy[direction] + dy[(direction+i)%4]
        if exit_board(nx,ny) == True:
            ret_value += tmp
            continue
        graph[nx][ny] += tmp
    return ret_value

def seven_percent(graph,start,direction):
    vx,vy = start
    tmp = (graph[vx][vy] * 7) // 100
    ret_value = 0
    for i in [-1,1]:
        nx = vx + dx[(direction+i)%4]
        ny = vy + dy[(direction+i)%4]
        if exit_board(nx,ny) == True:
            ret_value += tmp
            continue
        graph[nx][ny] += tmp
    return ret_value

def five_percent(graph,start,direction):
    vx,vy = start
    tmp = graph[vx][vy] // 20
    nx = vx + dx[direction] * 2
    ny = vy + dy[direction] * 2       
    if exit_board(nx,ny) == True:
        return tmp
    graph[nx][ny] += tmp
    return 0

def two_percent(graph,start,direction):
    vx,vy = start
    tmp = graph[vx][vy] // 50
    ret_value = 0
    for i in [-1,1]:
        nx = vx + 2 * dx[(direction+i)%4]
        ny = vy + 2 * dy[(direction+i)%4]
        if exit_board(nx,ny) == True:
            ret_value += tmp
            continue
        graph[nx][ny] += tmp
    return ret_value

def one_percent(graph,start,direction):
    vx,vy = start
    tmp = graph[vx][vy] // 100
    ret_value = 0
    for i in [-1,1]:
        nx = vx + dx[(direction+i)%4] - dx[direction]
        ny = vy + dy[(direction+i)%4] - dy[direction]            
        if exit_board(nx,ny) == True:
            ret_value += tmp
            continue
        graph[nx][ny] += tmp
    return ret_value

if __name__ == "__main__":
    n = int(input())
    main()
