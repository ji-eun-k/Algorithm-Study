for tc in range(1, int(input())+1):
    n = int(input())
    island = list(zip(list(map(int, input().split())), list(map(int, input().split()))))
    e = float(input())
    INF = 0xffffffffffff
    team = [0]*n
    adj = [[] for _ in range(n)]
    for i in range(n-1):
        for j in range(i+1, n):
            w = ((island[i][0] - island[j][0])**2 + (island[i][1] - island[j][1])**2)**0.5
            adj[i].append((j, w))
            adj[j].append((i, w))

    dist = [INF]*(n+1)
    dist[0] = 0
    ans = 0
    for _ in range(n):
        min_d = INF
        min_v = -1
        for i in range(n):
            if dist[i] < min_d and not team[i]:
                min_d = dist[i]
                min_v = i

        team[min_v] = 1
        ans += min_d*min_d
        for node, w in adj[min_v]:
            if w < dist[node] and not team[node]:
                dist[node] = w

    print('#{} {}'.format(tc, round(ans*e)))

