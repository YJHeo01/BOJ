#https://www.acmicpc.net/problem/30804
#https://www.acmicpc.net/source/80297316
#투 포인터

def main():
    n = int(input())
    fruit_list = list(map(int,input().split()))
    left, right = 0,0 #막대에 아무것도 없다고 가정, right는 새로 꽂은 과일, left는 가장 마지막에 꽂은 과일을 나타내는 인덱스
    fruit_cnt = [0] * 10 #타입별로 과일이 몇개 있는지 체크해주는 리스트
    type_cnt = 0 #몇종류의 과일을 사용했는지 나타냄
    answer = 0
    while True:
        if right >= n:break
        if fruit_cnt[fruit_list[right]] == 0:
            type_cnt += 1
        fruit_cnt[fruit_list[right]] += 1
        if type_cnt >= 3:
            while True:
                if type_cnt <= 2:
                    break
                fruit_cnt[fruit_list[left]] -= 1
                if fruit_cnt[fruit_list[left]] == 0:
                    type_cnt -= 1
                left += 1
        right += 1
        answer = max(answer,right-left)
    print(answer)

if __name__ == "__main__":
    main()
