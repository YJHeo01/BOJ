#https://www.acmicpc.net/problem/2720
#https://www.acmicpc.net/source/72272854
t = int(input())

for _ in range(t):
    c = int(input())
    quarter = c // 25
    c -= quarter * 25
    dime = c // 10
    c -= dime * 10
    nickel = c // 5
    c -= nickel * 5
    penny = c
    print(quarter,dime,nickel,penny)
