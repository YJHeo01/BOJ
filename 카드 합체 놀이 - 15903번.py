#https://www.acmicpc.net/problem/15903
#https://www.acmicpc.net/source/71035578

n,m = map(int,input().split())
card_list = list(map(int,input().split()))

for _ in range(m):
    card_list.sort()
    card_list[0] += card_list[1]
    card_list[1] = card_list[0]

print(sum(card_list))
