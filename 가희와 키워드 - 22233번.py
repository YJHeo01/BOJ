#https://www.acmicpc.net/problem/22233
#https://www.acmicpc.net/source/81062465

import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    memo = set([])
    for _ in range(n):
        memo.add(input().rstrip())
    for _ in range(m):
        array = list(input().rstrip().split(','))
        for s in array:
            if s in memo:
                memo.remove(s)
        print(len(memo))
    
if __name__ == "__main__":
    main()
