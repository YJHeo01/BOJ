#https://www.acmicpc.net/problem/32935
#https://www.acmicpc.net/source/87300141
#원소의 값을 바꾸는 시행을 할 경우, 값의 변화량은 -S-a_i이라고 볼 수 있다.
#따라서, -S-a_i가 양수인 경우 계속 시행을 하고, 그렇지 못하다면 시행을 중단한다.

n = int(input())

array = list(map(int,input().split()))

sum_value = sum(array)

for i in range(n):
    while True:
        tmp = -sum_value - array[i]
        if tmp <= 0:
            break
        sum_value -= array[i]
        array[i] += tmp
        sum_value += array[i]

print(sum_value)
