#https://www.acmicpc.net/problem/23559
#https://www.acmicpc.net/source/86334514
#유형 : 우선순위 큐, 그리디
#5000원 메뉴와 1000원 메뉴의 맛의 차이가 가장 큰 순서대로 5000원 메뉴를 섭취하고, 돈이 부족해서 5000원 메뉴를 섭취할 수 없거나, 1000원 메뉴가 더 맛있는 경우만 남을 경우 1000원 메뉴들만 섭취한다.
import sys, heapq

input = sys.stdin.readline

def main():
    q = []
    n,x = map(int,input().split())
    answer = 0
    for _ in range(n):
        a,b = map(int,input().split())
        heapq.heappush(q,(b-a,a,b))
    for i in range(n):
        tmp,a,b = heapq.heappop(q)
        if tmp >= 0 or 5000 + 1000 * (n-1-i) > x:
            answer += b
            break
        answer += a
        x -= 5000
    while q:
        tmp,a,b = heapq.heappop(q)
        answer += b
    print(answer)

if __name__ == "__main__":
    main()
