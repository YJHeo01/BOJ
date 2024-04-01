#https://www.acmicpc.net/problem/15651
#https://www.acmicpc.net/source/76115871

n,m = map(int,input().split())

def backtracking(array):
    if len(array) == m:
        for i in array:
            print(i,end=" ")
        print()
        return
    else:
        for i in range(1,n+1):
            backtracking(array + [i])

backtracking([])
