#https://www.acmicpc.net/problem/1806

n, c = map(int,input().split())

thing = list(map(int,input().split()))
answer = 100001 # 문제에서 주어진 수열의 최대 길이는 100000이므로, 초기값을 그보다 약간 큰 수로 지정해줬다.
left = 0
right = 1
tmp = sum(thing[0:1])
while left < n and right < n:
    if tmp >= c:
        tmp -= thing[left]
        answer = min(answer,(right-left))
        left += 1       
    else:
        tmp += thing[right]
        right+=1
if right == n:
    while left < n:
        if tmp >= c:
            tmp -= thing[left]
            answer = min(answer,(right-left))
            left += 1
        else:
            break 
    
if answer == 100001: #합을 만드는게 불가능한 경우
    answer = 0

print(answer)
