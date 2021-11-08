from collections import deque

dy = [0, 0, 1, -1, 1, -1, 1, -1]
dx = [1, -1, 0, 0, 1, -1, -1, 1]

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    maps = [list(map(int, input().split())) for _ in range(h)]
    ans = 0
    q = deque()
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                q.append([i, j])
                maps[i][j] = 0
                while q:
                    y, x = q.popleft()
                    for k in range(8):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0 <= ny < h and 0 <= nx < w and maps[ny][nx] :
                            q.append([ny, nx])
                            maps[ny][nx] = 0
                ans += 1
    print(ans)