from collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


for tc in range(1, int(input())+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    cost = [[0xfffff for _ in range(n)] for _ in range(n)]
    cost[0][0] = 0
    q = deque([(0, 0)])
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < n:
                temp = 1
                if data[y][x] < data[ny][nx]:
                    temp += data[ny][nx] - data[y][x]
                if cost[ny][nx] > cost[y][x] + temp:
                    cost[ny][nx] = cost[y][x] + temp
                    q.append((ny, nx))
    print('#{} {}'.format(tc, cost[n-1][n-1]))