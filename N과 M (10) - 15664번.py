#https://www.acmicpc.net/problem/15664
#https://www.acmicpc.net/source/81611062

last_answer = []

def main():
    array = sorted(list(map(int,input().split())))
    solution(array,0,0,[])

def solution(array,cnt,idx,answer):
    if cnt == m:
        global last_answer
        if answer not in last_answer:
            print(*answer)
            last_answer.append(answer)
        return
    for next_idx in range(idx,n):
        solution(array,cnt+1,next_idx+1,answer+[array[next_idx]])

if __name__ == "__main__":
    n,m = map(int,input().split())
    main()
