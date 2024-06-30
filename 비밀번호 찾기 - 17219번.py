#https://www.acmicpc.net/problem/17219
#https://www.acmicpc.net/source/80298122

import sys

input = sys.stdin.readline

def main():
    n,m = map(int,input().split())
    memo = {}
    for _ in range(n):
        address, password = input().split()
        memo[address] = password
    for _ in range(m):
        print(memo[input().rstrip()])

if __name__ == "__main__":
    main()
