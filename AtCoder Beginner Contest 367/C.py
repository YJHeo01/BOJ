import sys

sys.setrecursionlimit(10**6)

def main():
    array = list(map(int,input().split()))
    backtracking(array,[],0)

def backtracking(array,answer,length):
    if length >= n:
        if sum(answer) % k == 0: print(*answer)
        return
    for i in range(1,array[length]+1):
        backtracking(array,answer+[i],length+1)

if __name__ == "__main__":
    n,k = map(int,input().split())
    main()
