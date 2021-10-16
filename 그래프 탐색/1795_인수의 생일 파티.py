import heapq


def dijkstra(start, graph):
    q = []
    dist = [INF] * (N + 1)
    dist[start] = 0
    heapq.heappush(q, (0, start)) # 우선순위 큐로 다익스트라 해결

    while q:
        w, node = heapq.heappop(q) # start 지점에서 가장 가까운 노드가 알아서 정렬되어 선택
        if w > dist[node]: # 만약 q에 들어가 있으나 q에 들어간 거리보다, 저장된 최단 거리가 짧을 경우 넘김
            continue
        for i in range(1, N+1): # 모든 정점에서 선택된 노드와 연결되어 있는지 여부 확인
            if dist[i] > w + graph[node][i]: # 출발지점~현재노드 거리 + 현재노드~해당정점 거리가, 출발지점~해당정점 거리보다 짧을 경우
                dist[i] = w + graph[node][i] # 갱신
                heapq.heappush(q, (dist[i], i)) # 큐에 추가해주고 이를 기준으로 다시 최단 거리 탐색

    return dist[1:]


for tc in range(1, int(input())+1):
    N, M, X = map(int, input().split())
    INF = 0xfffff
    goto = [[INF]*(N+1) for _ in range(N+1)]
    into = [[INF]*(N+1) for _ in range(N+1)]

    for _ in range(M):
        x, y, z = map(int, input().split())
        goto[x][y] = z # X에서 출발하는 인접행렬
        into[y][x] = z # X로 들어오는 인접행렬

    print('#{} {}'.format(tc, max([x + y for x, y in zip(dijkstra(X, goto), dijkstra(X, into))])))




