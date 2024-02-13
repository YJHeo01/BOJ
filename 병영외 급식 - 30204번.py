#https://www.acmicpc.net/problem/30204
#https://www.acmicpc.net/source/73306005
n,x = map(int,input().split())

member_list = list(map(int,input().split()))

member_sum = sum(member_list)

if member_sum % x == 0:
    print(1)
else:
    print(0)
