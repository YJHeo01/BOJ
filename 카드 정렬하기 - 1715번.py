#https://www.acmicpc.net/problem/1715
#https://www.acmicpc.net/source/71096453

import sys
import heapq

input = sys.stdin.readline

n = int(input())

card_list = []
answer = 0
for _ in range(n):
    heapq.heappush(card_list,int(input()))

for _ in range(n-1):
    a = heapq.heappop(card_list)
    b = heapq.heappop(card_list)
    tmp = a + b
    answer += tmp
    heapq.heappush(card_list,tmp)

print(answer)
