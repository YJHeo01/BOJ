#https://www.acmicpc.net/problem/17626
#https://www.acmicpc.net/source/78809387
#pypy3

def main():
    n = int(input())
    dp = [0] * (n+1)
    for i in range(1,n+1):
        dp[i] = i
    value = 1
    while True:
        value += 1
        num = value ** 2
        if num > n: break
        for i in range(num,n+1):
            dp[i] = min(dp[i-num]+1,dp[i])
    print(dp[n])

if __name__ == "__main__":
    main()
