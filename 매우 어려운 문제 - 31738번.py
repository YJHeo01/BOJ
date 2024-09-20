#https://www.acmicpc.net/problem/31738
#https://www.acmicpc.net/source/84092023

n,m = map(int,input().split())
if n >= m:
    print(0)
else:
    answer = 1
    for i in range(2,n+1):
        answer *= i
        answer %= m
        if answer == 0: break
    print(answer)
