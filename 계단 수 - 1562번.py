#https://www.acmicpc.net/problem/1562
#https://www.acmicpc.net/source/86985779
#dp

INF = 1000000000

n = int(input())

dp = [[[0]*4 for _ in range(10)] for _ in range(n)] #dp[(길이-1)][(마지막 자리수)][(0부터 9까지 등장했는지 판별)]

#각 자리수가 1 차이이므로, 0과 9를 방문했을 경우, 0부터 9까지의 숫자가 모두 등장한다.
# (0부터 9까지 등장했는지 판별) -> 0 : 방문 x, 1 : (0)만 등장 , 2 : (9)만 등장, 3 : 0,9 모두 등장

for i in range(1,9):
    dp[0][i][0] = 1

dp[0][9][2] = 1

for length in range(1,n):
    for j in range(4):
        dp[length][0][j|1] += dp[length-1][1][j]
    for i in range(1,9):
        for j in range(4):
            dp[length][i][j] = dp[length-1][i-1][j] + dp[length-1][i+1][j]
    for j in range(4):
        dp[length][9][j|2] += dp[length-1][8][j]

answer = 0

for i in range(10):
    answer += dp[n-1][i][3]
    answer %= INF

print(answer)
