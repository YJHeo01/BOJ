#https://www.acmicpc.net/problem/14912
#https://www.acmicpc.net/source/82455305

n,d = map(int,input().split())

d = str(d)
answer = 0

for i in range(1,n+1):
    num = str(i)
    for j in num:
        if j == d:
            answer += 1

print(answer)
