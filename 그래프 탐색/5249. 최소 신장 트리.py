import heapq


def find_parent(x):
    if p[x] != x:
        p[x] = find_parent(p[x])
    return p[x]


def union(x, y):
    a = find_parent(x)
    b = find_parent(y)
    if a==b:
        return
    else:
        p[b] = a


for tc in range(1, int(input())+1):
    INF = 0xffff
    v, e = map(int, input().split())
    data = []
    for _ in range(e):
        n1, n2, w = map(int, input().split())
        heapq.heappush(data, (w, n1, n2))

    p = [i for i in range(v+1)]
    result = 0
    while data:
        w, n1, n2 = heapq.heappop(data)
        if find_parent(n1) == find_parent(n2):
            continue
        else:
            union(n1, n2)
            result += w
    print('#{} {}'.format(tc, result))
