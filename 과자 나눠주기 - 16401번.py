#https://www.acmicpc.net/problem/16401
#https://www.acmicpc.net/source/71047259

m,n = map(int,input().split())

snacks = list(map(int,input().split()))


answer = 0
right = max(snacks)
left = 1
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for snack in snacks:
        cnt += (snack // mid)
    if cnt >= m:
        answer = max(answer,mid)
        left = mid + 1
    else:
        right = mid -1
print(answer)
