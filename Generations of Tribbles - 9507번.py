#https://www.acmicpc.net/problem/9507
#https://www.acmicpc.net/source/82478201

dp = [1] * 68
dp[2], dp[3] = 2,4
for i in range(4,68):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]
for _ in range(int(input())):
    print(dp[int(input())])
