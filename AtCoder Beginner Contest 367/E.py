def main():
    n,k = map(int,input().split())
    x = [0] + list(map(int,input().split()))
    a = [0] + list(map(int,input().split()))
    p = [[0]*(n+1) for _ in range(60)]
    for i in range(n+1): p[0][i] = x[i]
    for lv in range(1,60):
        for i in range(1,n+1):
            p[lv][i] = p[lv-1][p[lv-1][i]]
    q = list(range(n+1))
    for lv in range(60):
        if k % 2 == 1:
            for i in range(1,n+1):
                q[i] = p[lv][q[i]]
        k = k // 2
    for i in range(1,n+1):
        print(a[q[i]],end=" ")

if __name__ == "__main__":
    main()
