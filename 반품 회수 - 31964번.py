#https://www.acmicpc.net/problem/31964
#https://www.acmicpc.net/source/81110732

def main():
    n = int(input())
    house = list(map(int,input().split()))
    time = list(map(int,input().split()))
    answer = 0
    for i in range(n):
        answer = max(answer,max(house[i],time[i])+house[i])
    print(answer)

if __name__ == "__main__":
    main()
