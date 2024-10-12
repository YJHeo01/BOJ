#https://www.acmicpc.net/problem/16978
#https://www.acmicpc.net/source/85094636
import sys, math

input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int,input().split()))
    s = [0] * (2 ** (math.ceil(math.log2(n))+1))
    init(a,s,1,0,n-1)
    m = int(input())
    first_query = []
    second_query  = [[] for _ in range(m+1)]
    first_query_cnt, second_query_cnt = 0,0
    for _ in range(m):
        idx, *tmp = input().split()
        if idx == '1':
            first_query.append(tmp)
            first_query_cnt += 1
        else:
            k,i,j = tmp
            second_query[int(k)].append((second_query_cnt,int(i),int(j)))
            second_query_cnt += 1
    ans = [0] * second_query_cnt
    for first_query_idx in range(first_query_cnt):
        for idx,i,j in second_query[first_query_idx]:
            ans[idx] = query(s,1,i-1,j-1,0,n-1)
        i,v = first_query[first_query_idx]
        i,v = int(i), int(v)
        a[i-1] = v
        update(s,1,i-1,0,n-1,v)
    for idx,i,j in second_query[first_query_cnt]:
        ans[idx] = query(s,1,i-1,j-1,0,n-1)
    sys.stdout.write('\n'.join(map(str, ans)))

    
def init(a,s,node,start,end):
    if start == end:
        s[node] = a[end]
        return
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    init(a,s,l_node,start,mid)
    init(a,s,r_node,mid+1,end)
    s[node] = s[l_node] + s[r_node]

def update(s,node,target,start,end,value):
    if target > end or target < start: return
    if start == end:
        s[node] = value
        return
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    update(s,l_node,target,start,mid,value)
    update(s,r_node,target,mid+1,end,value)
    s[node] = s[l_node] + s[r_node]

def query(s,node,left,right,start,end):
    if start > right or end < left: return 0
    if left <= start and end <= right: return s[node]
    l_node = node * 2; r_node = l_node + 1
    mid = (start+end) // 2
    return query(s,l_node,left,right,start,mid) + query(s,r_node,left,right,mid+1,end)

if __name__ == "__main__":
    main()
