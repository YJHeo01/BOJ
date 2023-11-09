#https://www.acmicpc.net/problem/2470

n = int(input())

acid_base = list(map(int,input().split()))

acid_base.sort()
left = 0
right = n-1
answer = (0,0)
answer_value = int(3e9)
while left < right: #투 포인터
    tmp = acid_base[left] + acid_base[right]
    if abs(tmp) < abs(answer_value):
        answer = (left,right)
        answer_value = tmp
    if tmp>0:
        right-=1
    elif tmp<0:
        left+=1
    else:
        break #정답을 찾았음
print(acid_base[answer[0]], acid_base[answer[1]])
