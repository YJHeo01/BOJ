#https://www.acmicpc.net/problem/25049
#https://www.acmicpc.net/source/86913617
#dp
#같은 노래를 3번 이상 들을 수 없다 = 다시 듣는 구간이 겹칠 수 없다
#따라서, 다시 듣는 구간이 어디서부터 어디서 끝나는지 체크해줘야 함
#이를 위해, 2차원 dp를 사용
#dp[i][j]에서 j = 0 : 노래 반복 x
#j = 1 : i번째 노래 반복 구간에 i번째 노래가 속함
#j = 2 : 1번째 노래 반복 구간과 2번째 노래 반복 구간 사이에 i번째 노래가 속함
#j = 3 : 2번째 노래 반복 구간에 i번째 노래가 속함
#j = 4 : i번째 노래 이전에 2번째 반복 구간이 끝남

INF = int(1e15)

n = int(input())

array = list(map(int,input().split()))

dp = [[-INF]*(5) for _ in range(n+1)]

dp[0][0] = 0

for i in range(n):
    dp[i+1][0] = dp[i][0] + array[i]

for i in range(1,5):
    for j in range(n):
        dp[j+1][i] = max(dp[j][i],dp[j][i-1]) + (1+i%2) * array[j]

print(max(dp[n]))
