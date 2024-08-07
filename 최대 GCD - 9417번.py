#https://www.acmicpc.net/problem/9417
#https://www.acmicpc.net/source/82146731

import sys

input = sys.stdin.readline

def Euclidean(a, b):
    if b == 0:
        return a
    return Euclidean(b, a % b)

for _ in range(int(input())):
    array = sorted(list(map(int,input().split())))
    length = len(array)
    answer = 1
    for right in range(length):
        for left in range(right):
            answer = max(answer,Euclidean(array[right],array[left]))
    print(answer)
