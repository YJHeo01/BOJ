#https://www.acmicpc.net/problem/19598
#https://www.acmicpc.net/source/80494472

import sys, heapq

input = sys.stdin.readline

def main():
    n = int(input())
    array = []
    for _ in range(n):
        array.append(list(map(int,input().split())))
    array.sort()
    answer, tmp = 0,0
    q = []
    for i in range(n):
        start,end = array[i]
        tmp += 1
        while q:
            last_end = heapq.heappop(q)
            if start >= last_end:
                tmp -= 1
            else:
                heapq.heappush(q,last_end)
                break
        answer = max(answer,tmp)
        heapq.heappush(q,end)
    print(answer)
        
if __name__ == "__main__":
    main()
