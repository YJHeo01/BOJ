#https://www.acmicpc.net/problem/10999
#https://www.acmicpc.net/source/80432898

import sys, math

input = sys.stdin.readline

def main():
    n,m,k = map(int,input().split())
    a = [int(input()) for _ in range(n)]
    h = math.ceil(math.log2(n))
    tree_size = 1 << (h+1)
    tree = [0] * tree_size
    lazy = [0] * tree_size
    m += k
    init(a,tree,1,0,n-1)
    for _ in range(m):
        command, *q = map(int,input().split())
        if command == 1:
            left,right,value = q
            update_range(tree,lazy,1,0,n-1,left-1,right-1,value)
        else:
            left, right = q
            print(query(tree,lazy,1,0,n-1,left-1,right-1))

def init(a,tree,node,start,end):
    if start == end:
        tree[node] = a[end]
        return tree[node]
    mid = (start+end) // 2
    tree[node] = init(a,tree,node*2,start,mid) + init(a,tree,node*2+1,mid+1,end)
    return tree[node]

def update_range(tree,lazy,node,start,end,left,right,value):
    if lazy[node] != 0: update_lazy(tree,lazy,node,start,end)
    if left > end or right < start: return
    if left <= start and end <= right:
        tree[node] += (end-start+1) * value
        if start != end:
            lazy[node*2] += value
            lazy[node*2+1] += value
        return
    mid = (start+end) // 2
    update_range(tree,lazy,node*2,start,mid,left,right,value)
    update_range(tree,lazy,node*2+1,mid+1,end,left,right,value)
    tree[node] = tree[node*2] + tree[node*2+1]

def update_lazy(tree,lazy,node,start,end):
    tree[node] += (end-start+1) * lazy[node]
    if start != end:
        lazy[node*2] += lazy[node]; lazy[node*2+1] += lazy[node]
    lazy[node] = 0

def query(tree,lazy,node,start,end,left,right):
    if lazy[node] != 0: update_lazy(tree,lazy,node,start,end)
    if left > end or right < start: return 0
    if left <= start and end <= right: return tree[node]
    mid = (start+end) // 2
    return query(tree,lazy,node*2,start,mid,left,right) + query(tree,lazy,node*2+1,mid+1,end,left,right)
            
if __name__ == "__main__":
    main()
