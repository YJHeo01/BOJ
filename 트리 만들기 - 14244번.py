#https://www.acmicpc.net/problem/14244
#https://www.acmicpc.net/source/86000495

n,m=map(int,input().split())
for i in range(n-m):print(i,i+1)
for i in range(m-1):print(n-m,n-i-1)
