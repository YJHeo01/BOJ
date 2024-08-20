#https://www.acmicpc.net/problem/1092
#https://www.acmicpc.net/source/82726305

def main():
    n = int(input())
    limit = sorted(list(map(int,input().split())),reverse=True)
    m = int(input())
    box = sorted(list(map(int,input().split())),reverse=True)
    if box[0] > limit[0]:
        print(-1)
        return
    complete = [False] * m
    answer = 0
    while True:
        finish = True
        limit_idx = 0
        for box_idx in range(m):
            if complete[box_idx] == True:
                continue
            finish = False
            if limit_idx >= n:
                break
            if limit[limit_idx] >= box[box_idx]:
                complete[box_idx] = True
                limit_idx += 1
        if finish == True:
            break
        answer += 1
    print(answer)

if __name__ == "__main__":
    main()
