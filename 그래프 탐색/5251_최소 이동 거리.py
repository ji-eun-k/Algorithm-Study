for tc in range(1, int(input())+1):
    N, E = map(int, input().split())
    INF = 0xffff
    data = [[INF]*(N+1) for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        data[s][e] = w
    dist = data[0][:]
    visited = [0]*(N+1)
    visited[0] = 1
    U = {0}
    while len(U) < N:
        min_v = 0xfffff
        min_idx = -1
        for i in range(N+1):
            if not visited[i] and min_v > dist[i]:
                min_v = dist[i]
                min_idx = i
        visited[min_idx] = 1
        U.add(min_idx)

        for i in range(N+1):
            if not visited[i] and data[min_idx][i] + dist[min_idx] < dist[i]:
                dist[i] = data[min_idx][i] + dist[min_idx]

    print('#{} {}'.format(tc, dist[N]))