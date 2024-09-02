#https://www.acmicpc.net/problem/31529
#https://www.acmicpc.net/source/83296515

x,y = map(int,input().split())
answer = 1012 * x - 506 * y
if 2*x < y or y < x:
    answer = -1
print(answer)
