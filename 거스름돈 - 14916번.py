#https://www.acmicpc.net/problem/14916
#https://www.acmicpc.net/source/71170409
n = int(input())

answer = -1

for i in range(n//5,-1,-1):
    if (n - 5 * i) % 2 == 0:
        answer = i + (n-5*i) // 2
        break
print(answer)
