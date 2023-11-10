#https://www.acmicpc.net/problem/1027

n = int(input())

tower = list(map(float,input().split()))

answer = 0
for i in range(n):
    block = 0 #이 변수가 1이 된다는 것은 건물이 안보인다는 것을 상징
    num = 0
    for j in range(i-1,-1,-1):
        for k in range(i-1,j,-1): # j = k = i-1일때는 실행이 안되지만 괜찮다. 어차피 이런 상황에서는 무조건 건물이 보이기 때문이다.
            line = tower[i] + (tower[j]-tower[i]) * (k-i) / (j-i) # 선분
            if tower[k] >= line: #선분이 건물에 접하거나 지나갈 경우
                block = 1
                break
        if block == 1:
            block = 0
        else:
            num+=1 
    block = 0
    for j in range(i+1,n):
        for k in range(i+1,j):
            line = tower[i] + (tower[j]-tower[i]) *(k-i)/ (j-i)
            if tower[k] >= line:
                block = 1
                break
        if block == 1:
            block = 0
        else:
            num+=1
    answer = max(answer,num)

print(answer)
