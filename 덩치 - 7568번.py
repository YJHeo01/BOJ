#https://www.acmicpc.net/problem/7568

N = int(input())
ranking = [1]*N #기본적으로 덩치가 더 큰 사람이 없으면 1등
xy = []
for i in range(N):
    x, y = map(int,input().split())
    xy.append((x,y))

for i in range(N):
    for j in range(N):
        if xy[i][0] < xy[j][0]:
            if xy[i][1] < xy[j][1]:
                ranking[i] += 1 # 몸무게, 키 모두 앞서는 사람이 있을 경우 순위가 밀림

for i in range(N):
    print(ranking[i], end=' ')
