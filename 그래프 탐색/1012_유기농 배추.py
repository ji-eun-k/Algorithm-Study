from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def dfs(y, x):
    q = deque([(y, x)])
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dy[d]
            nc = c + dx[d]
            if 0<=nr<n and 0<=nc<m and maps[nr][nc]:
                maps[nr][nc] = 0
                q.append((nr, nc))


for tc in range(int(input())):
    m, n, k = map(int, input().split())
    maps = [[0]*m for _ in range(n)]
    worm = 0
    for _ in range(k):
        x, y = map(int, input().split())
        maps[y][x] = 1

    for i in range(n):
        for j in range(m):
            if maps[i][j] :
                worm += 1
                dfs(i, j)
    print(worm)