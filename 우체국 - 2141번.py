#https://www.acmicpc.net/problem/2141
#https://www.acmicpc.net/source/71411160
#https://github.com/YJHeo01

import sys
input = sys.stdin.readline
n = int(input())

distance_sum_LtoR = [0] * (n+1)
distance_sum_RtoL = [0] * (n+1)
human_sum_LtoR = [0] * (n+1)
human_sum_RtoL = [0] * (n+1)

town_information = []

for i in range(1,n+1):
    town_information.append(list(map(int,input().split())))

town_information.sort()

town_information = [[0,0]] + town_information
for i in range(2,n+1):
    human_sum_LtoR[i] = human_sum_LtoR[i-1] + town_information[i-1][1]
    distance_sum_LtoR[i] = distance_sum_LtoR[i-1] + (human_sum_LtoR[i]) * (town_information[i][0] - town_information[i-1][0])

for i in range(n-1,0,-1):
    human_sum_RtoL[i] = human_sum_RtoL[i+1] + town_information[i+1][1]
    distance_sum_RtoL[i] = distance_sum_RtoL[i+1] + human_sum_RtoL[i] * (town_information[i+1][0] - town_information[i][0])

answer = town_information[1][0]
min_sum_distance = distance_sum_LtoR[1] + distance_sum_RtoL[1]

for i in range(2,n+1):
    tmp = distance_sum_LtoR[i] + distance_sum_RtoL[i]
    if min_sum_distance > tmp:
        min_sum_distance = tmp
        answer = town_information[i][0]

print(answer)
