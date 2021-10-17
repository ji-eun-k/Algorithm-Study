import heapq

for tc in range(1, int(input())+1):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())
    INF = 0xffffffffff
    team = [0]*n
    adj = [[INF]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            adj[i][j] = adj[j][i] = ((y[i] - y[j])**2 + (x[i] - x[j])**2)*e

    q = []
    heapq.heappush(q, (0, 0))
    ans = 0
    while q:
        w, v = heapq.heappop(q)
        if team[v]:
            continue
        team[v] = 1
        ans += w
        for i in range(n):
            if not team[i] and adj[v][i] < INF:
                heapq.heappush(q, (adj[v][i], i))

    print('#{} {}'.format(tc, round(ans)))
