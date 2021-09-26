from collections import deque

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    maps = [input() for _ in range(n)]
    answer = 0
    q = deque()
    visited = [[-1]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'W':
                visited[i][j] = 0
                q.append((i, j))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m and maps[ny][nx]=='L' and visited[ny][nx] == -1 :
                q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1

    for i in visited:
        for j in i:
            answer += j

    print('#{} {}'.format(tc, answer))