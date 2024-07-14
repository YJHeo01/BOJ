#https://www.acmicpc.net/problem/32029
#https://www.acmicpc.net/source/81009818

import sys

input = sys.stdin.readline


def main():
    n,a,b = map(int,input().split())
    array = list(map(int,input().split()))
    array.sort()
    answer = 0
    for x in range(a):    
        for i in range(n):
            cnt = 0
            time = a
            for j in range(i):
                if time <= array[j]:
                    cnt += 1
                    time += a
            time += b * x
            time -= x
            for j in range(i,n):
                if time <= array[j]:
                    cnt += 1
                    time += (a-x)
            answer = max(answer,cnt)
    print(answer)

if __name__ == "__main__":
    main()
