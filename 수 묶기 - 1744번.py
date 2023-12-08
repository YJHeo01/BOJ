#https://www.acmicpc.net/problem/1744
#https://www.acmicpc.net/source/70145252
#greedy 알고리즘, 우선순위 큐 이용
import heapq



n = int(input())

def heappush(value):
    global minus_value_list,plus_value_list
    if value > 0:
        heapq.heappush(plus_value_list,-value)
    else:
        heapq.heappush(minus_value_list,value)

for _ in range(n):
    value = int(input())
    heappush(value)

def sum_value(num_list,plus_minus):
    return_value = 0
    while len(num_list)>=2:
        value1 = (-plus_minus)*heapq.heappop(num_list)
        value2 = (-plus_minus)*heapq.heappop(num_list)
        return_value += max((value1*value2),(value1+value2)) #대부분 절댓값이 큰 수 끼리 곱하는게 제일 크지만 -1,0,1이 섞인 경우에는 서로 더하는 것이 가장 큰 경우가 있다.
    if num_list != []:
        return (return_value,num_list[0])
    else:
        return (return_value,0)

def sum_minus_value(num_list):
    value1, value2 = sum_value(num_list,-1)
    return (value1+value2)

def sum_plus_value(num_list):
    value1, value2 = sum_value(num_list,1)
    return (value1-value2)

def find_answer():
    value1 = sum_minus_value(minus_value_list)
    value2 = sum_plus_value(plus_value_list)
    return (value1+value2)

minus_value_list = [] #0도 이 리스트에 저장한다.
plus_value_list = []

answer = find_answer()

print(answer)
