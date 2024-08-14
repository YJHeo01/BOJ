#https://www.acmicpc.net/problem/5623
#https://www.acmicpc.net/source/82455942

import sys

input = sys.stdin.readline

n = int(input())

if n == 2:
    print("1 1") #n이 2일 경우 입력으로 주어지는 S에 해당하는 수열 A는 항상 유일한 경우는 이거밖에 없음
    exit(0)

matrix = [list(map(int,input().split())) for _ in range(n)]

a = [0] * n

a[1] = (matrix[0][1] + matrix[1][2] - matrix[0][2]) // 2
a[0] = matrix[0][1] - a[1]

for i in range(2,n):
    a[i] = matrix[i][i-1] - a[i-1]

print(*a)
