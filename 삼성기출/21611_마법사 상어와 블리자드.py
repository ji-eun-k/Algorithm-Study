from collections import deque
# d -1 해주어야 함
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

qy = [0, 1, 0, -1]
qx = [-1, 0, 1, 0]

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
for _ in range(m):
    d, s = map(int, input().split())
    y, x = n//2, n//2
    for _ in range(s): # 블리자드
        ny = y+dy[d-1]
        nx = x+dx[d-1]
        if 0>ny or 0>nx or n<=ny or n<=nx:
            break
        grid[ny][nx] = 0
        y = ny
        x = nx

    y, x = n//2, n//2
    q = deque()
    dire = 0
    cnt = 0
    turn = 0
    move = 1
    jungbok = [0, 0, 0, 0] # 0, 1, 2, 3
    flag = 0

    while True:
        ny = y + qy[dire]
        nx = x + qx[dire]
        cnt += 1
        if grid[ny][nx]:
            q.append(grid[ny][nx])
        if ny == 0 and nx == 0:
            break

        if cnt == move:
            cnt = 0
            turn += 1
            dire = (dire+1) % 4
            if turn % 2 == 0:
                turn = 0
                move += 1
        y, x = ny, nx
    print(q)
    # 4개 체크 + 폭발 - while / flag



