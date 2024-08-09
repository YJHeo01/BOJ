#https://www.acmicpc.net/problem/1793
#https://www.acmicpc.net/source/82246108

dp_a, dp_b, dp_c = [0] * 251, [0] * 251, [0] * 251

dp_a[1], dp_b[2], dp_a[2], dp_c[2] = 1,1,1,1

for i in range(3,251):
    dp_a[i] = dp_a[i-1] + dp_b[i-1] + dp_c[i-1]
    dp_b[i] = dp_a[i-2] + dp_b[i-2] + dp_c[i-2]
    dp_c[i] = dp_a[i-2] + dp_b[i-2] + dp_c[i-2]

while True:
    try:
        n = int(input())
        if n == 0:
            print(1)
            continue
        print(dp_a[n]+dp_b[n]+dp_c[n])
    except EOFError:
        break
