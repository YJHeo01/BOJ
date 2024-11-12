#https://www.acmicpc.net/problem/27172
#https://www.acmicpc.net/source/86343549
n = int(input())

INF = 1000001

exist = [False] * INF

array = list(map(int,input().split()))

for i in array: exist[i] = True

score = [0] * INF

for i in array:
    for j in range(i+i,INF,i):
        if exist[j]:
            score[i] += 1
            score[j] -= 1

for i in array: print(score[i],end=" ")
