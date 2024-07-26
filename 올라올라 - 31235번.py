#https://www.acmicpc.net/problem/31235
#https://www.acmicpc.net/source/81628347

n = int(input())

array = list(map(int,input().split()))

answer = 0
max_value, max_idx = 0,-1

for i in range(n):
    if array[i] >= max_value:
        answer = max(i-max_idx,answer)
        max_value = array[i]
        max_idx = i
answer = max(answer,n-max_idx)
print(answer)
