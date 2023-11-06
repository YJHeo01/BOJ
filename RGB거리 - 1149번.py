#https://www.acmicpc.net/problem/1149
import sys

input = sys.stdin.readline

n = int(input())
dp = [[0]*3 for _ in range(n)]
house = [] # 각 집을 칠할 때 필요한 비용을 저장
for i in range(n):
    tmp = list(map(int,input().split()))
    house.append(tmp)

if n == 2:
    print(max(house[0][0]+house[1][1],house[0][0]+house[1][2],house[0][1]+house[1][0],house[0][1]+house[1][2],house[0][2]+house[1][1],house[0][2]+house[1][0]))
else:
    dp[0][0],dp[0][1],dp[0][2] = house[0][0],house[0][1],house[0][2]
    dp[1][0] = min(dp[0][1]+house[1][0],dp[0][2]+house[1][0])
    dp[1][1] = min(dp[0][0]+house[1][1],dp[0][2]+house[1][1])
    dp[1][2] = min(dp[0][1]+house[1][2],dp[0][0]+house[1][2])
    for i in range(2,n):
        dp[i][0] = house[i][0] + min(house[i-1][1]+dp[i-2][0],house[i-1][2]+dp[i-2][0],house[i-1][1]+dp[i-2][2],house[i-1][2]+dp[i-2][1]) #i번째 집을 붉은 색으로 칠할 때 비용의 합 중 최솟값
        dp[i][1] = house[i][1] + min(house[i-1][0]+dp[i-2][1],house[i-1][2]+dp[i-2][1],house[i-1][0]+dp[i-2][2],house[i-1][2]+dp[i-2][0]) #i번째 집을 초록 색으로 칠할 때 비용의 합 중 최솟값
        dp[i][2] = house[i][2] + min(house[i-1][1]+dp[i-2][2],house[i-1][0]+dp[i-2][2],house[i-1][1]+dp[i-2][0],house[i-1][0]+dp[i-2][1]) #i번째 집을 푸른 색으로 칠할 때 비용의 합 중 최솟값

print(min(dp[n-1]))
