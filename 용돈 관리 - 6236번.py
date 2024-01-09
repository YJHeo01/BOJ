#https://www.acmicpc.net/problem/6236
#https://www.acmicpc.net/source/71427653
#https://github.com/YJHeo01
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
money_day = []
for _ in range(n):
    money_day.append(int(input()))

left = min(money_day)
right = sum(money_day)
max_money = max(money_day)
k = int(1e9)

while left <= right:
    mid = (left + right) // 2
    tmp = mid
    find_money_cnt = 1
    if mid < max_money:
        left = mid + 1
        continue
    for money in money_day:
        if money > tmp:
            find_money_cnt += 1
            tmp = mid - money
        else:
            tmp -= money
    if find_money_cnt <= m:
        k = min(mid,k)
        right = mid -1
    else:
        left = mid + 1

print(k)
