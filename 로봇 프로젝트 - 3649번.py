#https://www.acmicpc.net/problem/3649
#https://www.acmicpc.net/source/74059385
import sys

input = sys.stdin.readline

while True:
    x = input()
    if x == "":
        break
    x = int(x)
    x *= 10000000
    n = int(input())
    lego_list = []
    for _ in range(n):
        lego_list.append(int(input()))
    lego_list.sort()
    right = n-1
    left = 0
    danger = True
    l1, l2 = 0,0
    while left < right:
        if lego_list[left] + lego_list[right] > x:
            right -= 1
        elif lego_list[left] + lego_list[right] < x:
            left += 1
        else:
            danger = False
            l1, l2 = lego_list[left],lego_list[right]
            break
    if danger == True:
        print('danger')
    else:
        print('yes', l1, l2)      
