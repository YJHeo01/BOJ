#구현, 시뮬레이션 문제
#지문에 있는 그대로 구현을 해주면 된다.
#다만, 한번에 월급을 두 번 받는 이동도 고려를 해줘야 한다.
#나중에 리팩토링 한번 해서 다시 업로드할듯싶다.
#https://www.acmicpc.net/problem/28457
#https://www.acmicpc.net/source/86147735
import sys

input = sys.stdin.readline

def main():
    n,s,w,g = map(int,input().split())
    city_buy = [False] * (4*n-4)
    golden_card = []
    for _ in range(g): golden_card.append(list(map(int,input().split())))
    unicef = 0
    state = [0] * (4*n - 4)
    for i in range(4):
        state[i*(n-1)] = -i
        city_buy[i*(n-1)] = True
        for j in range(n-2):
            tmp = list(input().split())
            position = i*(n-1)+j+1
            #print(position)
            if tmp[0] == 'G':
                state[position] = -5
                city_buy[position] = True
            else:
                state[position] = int(tmp[1])
    i = int(input())
    block_cnt = 0
    cur_position = 0
    cur_money = s
    card_idx = 0
    answer = 'WIN'
    for _ in range(i):
        a,b = map(int,input().split())
        if cur_money < 0: answer = 'LOSE'
        if block_cnt != 0:
            if a == b: block_cnt = 0
            else: block_cnt -= 1
            continue
        cur_position += (a+b)
        while True:
            if cur_position < 4 * (n-1): break
            cur_money += w
            cur_position -= 4 * (n-1)
        if state[cur_position] >= 0:
            if city_buy[cur_position]: continue
            if cur_money >= state[cur_position]:
                cur_money -= state[cur_position]
                city_buy[cur_position] = True
        elif state[cur_position] == -1:
            block_cnt = 3
        elif state[cur_position] == -2:
            cur_money += unicef
            unicef = 0
        elif state[cur_position] == -3:
            cur_position = 0
            cur_money += w
        else:
            command, value = golden_card[card_idx]
            card_idx += 1; card_idx %= g
            if command == 1: cur_money += value
            elif command == 2: cur_money -= value
            elif command == 3: unicef += value; cur_money -= value
            else: 
                cur_position += value
                while True:
                    if cur_position < 4 * (n-1): break
                    cur_money += w
                    cur_position -= (4 * (n-1))
                if state[cur_position] >= 0:
                    if city_buy[cur_position] or state[cur_position] > cur_money: continue
                    cur_money -= state[cur_position]
                    city_buy[cur_position] = True
                elif state[cur_position] == -1: block_cnt = 3
                elif state[cur_position] == -2: cur_money += unicef; unicef = 0
                else: cur_position = 0; cur_money += w
        if cur_money < 0: answer = 'LOSE'
    for i in range(4*n-4):
        if city_buy[i] == False: answer = 'LOSE'
    print(answer)

if __name__ == "__main__":
    main()
