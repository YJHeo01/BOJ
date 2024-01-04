#https://www.acmicpc.net/problem/1449
#https://www.acmicpc.net/source/71167503
#https://github.com/YJHeo01/

n,l = map(int,input().split())

hole = list(map(int,input().split()))

hole.sort()

left_hole = 0
right_hole = 0

answer = 1

while right_hole < n:
    if hole[right_hole] - hole[left_hole] < l:
        right_hole += 1
    else:
        answer += 1
        left_hole = right_hole

print(answer)
