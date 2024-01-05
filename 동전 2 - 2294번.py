#https://www.acmicpc.net/problem/2294
#https://www.acmicpc.net/source/71225187
#https://github.com/YJHeo01

n,k = map(int,input().split())

coin_list = []

for _ in range(n):
    coin_list.append(int(input()))

INF = int(1e9)
dp = [INF] * (k+1)
dp[0] = 0

for coin in coin_list:
    for i in range(coin,k+1):
        if dp[i] > dp[i-coin] + 1:
            dp[i] = dp[i-coin] + 1
if dp[k] == INF:
    dp[k] = -1
print(dp[k])
