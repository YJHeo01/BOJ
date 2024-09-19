def main():
    n,m = map(int,input().split())
    array = list(map(int,input().split()))
    distance = [0]
    for i in range(2*n):
        distance.append((distance[-1]+array[i%n])%m)
    cnt = [0] * m
    for i in range(n):
        cnt[distance[i]] += 1
    answer = 0
    for i in range(n,2*n):
        cnt[distance[i-n]] -= 1
        answer += cnt[distance[i]]
        cnt[distance[i]] += 1
    print(answer)

if __name__ == "__main__":
    main()
