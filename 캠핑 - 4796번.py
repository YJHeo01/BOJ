#https://www.acmicpc.net/problem/4796
#https://www.acmicpc.net/source/74062947

case_idx = 1

while True:
    l,p,v = map(int,input().split())
    if l == 0 and p == 0 and v == 0:
        break
    answer = (v//p) * l + min(v % p,l)
    print("Case " + str(case_idx) + ": " + str(answer))
    case_idx += 1
