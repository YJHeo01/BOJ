#https://www.acmicpc.net/problem/2217
import sys
input = sys.stdin.readline

n = int(input())
answer = 0
ropes = []
for i in range(n):
    tmp = int(input())
    ropes.append(tmp)
ropes.sort(reverse=True)
for i in range(1,n+1):
    tmp = ropes[i-1] * (i) #k개의 로프를 사용했을 때, 가장 약한 로프가 버틸수 있는 한계
    if tmp > answer:
        answer = tmp
print(answer)
