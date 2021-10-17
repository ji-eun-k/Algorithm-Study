from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def dfs(start_y, start_x):
    q = deque([(start_y, start_x, 0)])
    dist[start_y][start_x] = 0

    while q:
        now_y, now_x, my_dist = q.popleft()       # 현재 y 좌표, 현재 x 좌표, dist 갱신 전에 저장한 거리

        if my_dist > dist[now_y][now_x]:          # 만약, dist 갱신 전에 저장한 거리가 다른 곳에서 갱신된 거리보다 길면
            continue                              # 굳이 살펴볼 이유가 없으므로(최단 거리가 x) continue

        for k in range(4):
            ny = now_y + dy[k]
            nx = now_x + dx[k]
            # 현재 살펴보는 정점을 거쳐서 가는 ny, nx 의 거리가 이전에 ny, nx에 저장된 거리보다 짧으면 갱신
            if 0 <= ny < N and 0 <= nx < N and dist[ny][nx] > maps[ny][nx] + my_dist:
                dist[ny][nx] = maps[ny][nx] + my_dist
                q.append((ny, nx, dist[ny][nx]))  # 현재 시점에서 이 정점을 거처야 최단 거리이므로 큐에 추가


for tc in range(1, int(input())+1):
    N = int(input())
    maps = [[int(i) for i in input()] for _ in range(N)]
    dist = [[float('inf')]*N for _ in range(N)]   # 거리정보 무한대로 초기화
    dfs(0, 0)
    print('#{} {}'.format(tc, dist[N-1][N-1]))
