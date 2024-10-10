#https://www.acmicpc.net/problem/16112
#https://www.acmicpc.net/source/85008100

n,k = map(int,input().split())
array = sorted(list(map(int,input().split())))
answer = 0
for i in range(n):
    answer += array[i] * min(i,k)
print(answer)
