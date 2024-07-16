#https://www.acmicpc.net/problem/1094
#https://www.acmicpc.net/source/81122689
#각 막대기는 2의 n제곱의 길이를 얻을 수 있다.(n>=0) 단, 64보단 짧다
def main():
    answer = 0
    x = int(input())
    for i in range(7):
        if x & (2**i) != 0: answer += 1
    print(answer)
        
if __name__ == "__main__":
    main()
