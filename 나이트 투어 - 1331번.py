#https://www.acmicpc.net/problem/1331
#https://www.acmicpc.net/source/71038573

def ChrToNum(point):
    x = ord(point[0]) - ord('A')
    y = int(point[1]) - 1
    return (x,y)

first_point = list(input())

first_point = ChrToNum(first_point)
last_point = first_point
visited_board = [[False]*6 for _ in range(6)]
visited_board[first_point[0]][first_point[1]] = True
Valid = True

def check_knight_move(point1, point2):
    move_list = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
    for move in move_list:
        if point1[0] == (point2[0] + move[0]) and point1[1] == (point2[1] + move[1]):
            return True
    return False

for _ in range(35):
    point = ChrToNum(list(input()))
    if check_knight_move(last_point,point) == False or visited_board[point[0]][point[1]] == True:
        Valid = False #나이트의 움직임이 아니거나, 정확히 한 번씩 방문하지 않는 경우 Invalid
    visited_board[point[0]][point[1]] = True
    last_point = point

if check_knight_move(first_point,last_point) == False:
    Valid = False #나이트의 도착지가 시작 점인지 체크

if Valid == False:
    print("Invalid")
else:
    print("Valid")
