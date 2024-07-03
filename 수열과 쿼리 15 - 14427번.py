#https://www.acmicpc.net/problem/14427
#https://www.acmicpc.net/source/80431309

import sys, heapq

input = sys.stdin.readline

def main():
    n = int(input())
    array = [0] + list(map(int,input().split())) #현재 수열에서의 인덱스별 값을 저장
    q = []
    for i in range(1,n+1):
        heapq.heappush(q,(array[i],i)) #우선순위 큐를 활용하여 가장 작은 값의 인덱스를 출력
    m = int(input())
    for _ in range(m):
        tmp = list(map(int,input().split()))
        if tmp[0] == 1:
            heapq.heappush(q,(tmp[2],tmp[1]))
            array[tmp[1]] = tmp[2]
        else:
            while True:
                value, idx = heapq.heappop(q) #우선순위큐에서의 pop연산을 통해 가장 작은 값과 그 값의 인덱스를 꺼냄
                if array[idx] == value: #이때, value가 array[idx]의 현재 값이 아닌 과거의 값이라면 무시
                    print(idx)
                    heapq.heappush(q,(value,idx))
                    break
    

if __name__ == "__main__":
    main()
