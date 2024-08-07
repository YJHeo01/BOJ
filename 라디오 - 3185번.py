#https://www.acmicpc.net/problem/3135
#https://www.acmicpc.net/source/82146371

a,b = map(int,input().split())
n = int(input())
array = [int(input()) for _ in range(n)]
answer = abs(a-b)
for i in array:
    answer = min(answer,abs(b-i)+1)
print(answer)
