#https://www.acmicpc.net/problem/9944
#https://www.acmicpc.net/source/77658138
#pypy3
INF = int(1e9)

def main():
    case_idx = 0
    while True:
        try:
            case_idx += 1
            global n,m
            n,m = map(int,input().split())
            board = []
            for _ in range(n):
                board.append(list(input()))
            answer = INF
            for i in range(n):
                for j in range(m):
                    if board[i][j] == '*':
                        continue
                    visited = get_init_visited(board)
                    answer = min(answer,solution(visited,(i,j),1))
            if answer >= INF:
                answer = -1
            print("Case " + str(case_idx) + ": " + str(answer))
        except EOFError:
            break

def get_init_visited(board):
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == '*':
                visited[i][j] = True
    return visited
    
def solution(visited,start,move_cnt):
    ret_value = INF
    ret_value_zero = True
    x,y = start
    if x > 0 and visited[x-1][y] == False:
        ret_value_zero = False
        new_start = move_ball(visited,start,(-1,0))
        if game_over(visited) == True: 
            cancel_move(visited,start,new_start,(-1,0))
            return move_cnt
        ret_value = min(ret_value,solution(visited,new_start,move_cnt+1))
        cancel_move(visited,start,new_start,(-1,0))

    if y > 0 and visited[x][y-1] == False:
        ret_value_zero = False
        new_start = move_ball(visited,start,(0,-1))
        if game_over(visited) == True:
            cancel_move(visited,start,new_start,(0,-1))
            return move_cnt
        ret_value = min(ret_value,solution(visited,new_start,move_cnt+1))
        cancel_move(visited,start,new_start,(0,-1))

    if x < n-1 and visited[x+1][y] == False:
        ret_value_zero = False
        new_start = move_ball(visited,start,(1,0))
        if game_over(visited) == True:
            cancel_move(visited,start,new_start,(1,0))
            return move_cnt
        ret_value = min(ret_value,solution(visited,new_start,move_cnt+1))
        cancel_move(visited,start,new_start,(1,0))

    if y < m-1 and visited[x][y+1] == False:
        ret_value_zero = False
        new_start = move_ball(visited,start,(0,1))
        if game_over(visited) == True:
            cancel_move(visited,start,new_start,(0,1))
            return move_cnt
        ret_value = min(ret_value,solution(visited,new_start,move_cnt+1))
        cancel_move(visited,start,new_start,(0,1))
    if move_cnt == 1 and ret_value_zero == True:
        ret_value = 0
    return ret_value

def move_ball(visited,start,direction):
    dx,dy = direction
    x,y = start
    while True:
        visited[x][y] = True
        nx = x + dx; ny = y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny] == True:
            return x,y
        x = nx; y = ny

def game_over(visited):
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False:
                return False
    return True

def cancel_move(visited,start,end,direction):
    x,y = start
    dx, dy = direction
    while True:
        x += dx
        y += dy
        visited[x][y] = False
        if x == end[0] and y == end[1]:
            return

if __name__ == "__main__":
    main()
