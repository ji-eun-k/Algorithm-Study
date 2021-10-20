# 거리가 가까운 물고기 많다면 가장 위, 왼쪽에 있는 물고기 먹기
import sys
from collections import deque
input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def bfs(y, x):
    global ans
    global baby_shark
    start_y = y
    start_x = x
    maps[start_y][start_x] = 0
    eat = 0
    while True:
        q = deque([[start_y, start_x, 0]])
        fish_pos = []
        check = False
        fish_dist = n*n+1
        visited = [[0]*n for _ in range(n)]
        visited[start_y][start_x] = 1
        while q:
            r, c, dist = q.popleft()
            for k in range(4):
                ny = r + dy[k]
                nx = c + dx[k]

                if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and maps[ny][nx] <= baby_shark:
                    visited[ny][nx] = 1
                    if (maps[ny][nx] == baby_shark or not maps[ny][nx]) and fish_dist > dist + 1:
                        q.append([ny, nx, dist+1])

                    if 0 < maps[ny][nx] < baby_shark:
                        if fish_dist > dist+1:
                            fish_dist = dist+1
                            fish_pos = [[ny, nx]]
                        elif fish_dist == dist + 1:
                            fish_pos.append([ny, nx])

        if len(fish_pos) > 0:
            fish_pos.sort()
            ny, nx = fish_pos[0]
            ans += fish_dist
            eat += 1
            maps[ny][nx] = 0
            if eat == baby_shark:
                baby_shark += 1
                eat = 0
            start_y = ny
            start_x = nx
        else:
            return





n = int(input())
# 1, 2, 3, 4, 5, 6 : 물고기 크기
# 9 아기 상어 위치
maps = [list(map(int, input().split())) for _ in range(n)]
baby_shark = 2
ans = 0

for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            bfs(i, j)
            break


print(ans)
