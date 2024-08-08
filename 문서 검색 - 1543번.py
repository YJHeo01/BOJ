#https://www.acmicpc.net/problem/1543
#https://www.acmicpc.net/source/82202159

import sys

sys.setrecursionlimit(10**6)

s = input()
target = input()
length = len(s)
target_length = len(target)

def backtracking(s,target,cnt,idx):
    if idx + target_length > length:
        return cnt
    elif s[idx:idx+target_length] == target:
        return backtracking(s,target,cnt+1,idx+target_length)
    else:
        return backtracking(s,target,cnt,idx+1)

print(backtracking(s,target,0,0))
