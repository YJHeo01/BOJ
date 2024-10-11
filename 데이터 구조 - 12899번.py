#https://www.acmicpc.net/problem/12899
#https://www.acmicpc.net/source/85051654

import sys, math

input = sys.stdin.readline

def main():
    n = int(input())
    length = 2 ** (math.ceil(math.log2(INF))+1)
    s = [0] * length
    ans = []
    for _ in range(n):
        t,x = map(int,input().split())
        if t == 1:
            update(s,1,x,0,INF-1)
        else:
            ans.append(query(s,1,0,INF-1,x))
    sys.stdout.write('\n'.join(map(str, ans)))

def update(s,node,target,start,end):
    if start > target or end < target:
        return
    if start == end:
        s[node] += 1
        return
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    update(s,l_node,target,start,mid)
    update(s,r_node,target,mid+1,end)
    s[node] = s[l_node] + s[r_node]

def query(s,node,start,end,value):
    if start == end:
        s[node] -= 1
        return end
    mid = (start+end) // 2
    l_node = node * 2; r_node = l_node + 1
    if s[l_node] >= value:
        ret_value = query(s,l_node,start,mid,value)
    else:
        ret_value = query(s,r_node,mid+1,end,value-s[l_node])
    s[node] = s[l_node] + s[r_node]
    return ret_value

if __name__ == '__main__':
    INF = 2000001
    main()
