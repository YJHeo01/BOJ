#https://www.acmicpc.net/problem/17088
#https://www.acmicpc.net/source/81059721
# 수열의 첫번째 값과 두번째 값을 각각 -1,0,1중 하나를 더해주고 나머지 수들의 값의 차이도 (수열의 두 번째 값) - (수열의 첫 번째 값)로 만들수 있는지 체크해준다.
def main():
    n = int(input())
    init_array = list(map(int,input().split()))
    if n == 1:
        print(0)
        return
    INF = int(1e9)
    answer = INF
    for i in range(-1,2):
        for j in range(-1,2):
            array = []
            for value in init_array: array.append(value)
            tmp = 0
            if i != 0: tmp += 1
            if j != 0: tmp += 1
            array[0] += i; array[1] += j
            for k in range(2,n):
                if array[k] + 1 - array[k-1] == array[1] - array[0]:
                    array[k] += 1
                    tmp += 1
                elif array[k] - 1 - array[k-1] == array[1] - array[0]:
                    array[k] -= 1
                    tmp += 1
                elif array[k] - array[k-1] == array[1] - array[0]:
                    continue
                else:
                    tmp = INF
                    break
            answer = min(answer,tmp)
    if answer >= INF:
        answer = -1
    print(answer)

if __name__ == "__main__":
    main()
