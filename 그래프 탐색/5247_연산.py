from collections import deque

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    q = deque([(n, 0)])
    min_count = 1000000
    check = [0]*1000001
    while q:
        x, w = q.popleft()
        if check[x]:
            continue
        check[x] = 1
        if x == m:
            min_count = w
        if w > min_count:
            continue
        if 0 < x + 1 <= 1000000:
            q.append((x+1, w+1))
        if 0 < x - 1 <= 1000000:
            q.append((x-1, w+1))
        if 0 < x * 2 <= 1000000:
            q.append((x*2, w+1))
        if 0 < x - 10 <= 1000000:
            q.append((x-10, w+1))
    print('#{} {}'.format(tc, min_count))