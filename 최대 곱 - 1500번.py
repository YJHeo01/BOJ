#https://www.acmicpc.net/problem/1500
#https://www.acmicpc.net/source/80097331

def main():
    s,k = map(int,input().split())
    array = []
    for _ in range(k):
        array.append(s//k)
    for i in range(s%k):
        array[i] += 1
    answer = 1
    for i in array:
        answer *= i
    print(answer)

if __name__ == "__main__":
    main()
