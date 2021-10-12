from copy import deepcopy
from collections import deque


def bomb(my_brick, bomb_j):
    new_brick = deepcopy(my_brick)
    q = deque()
    for bomb_i in range(h):
        if new_brick[bomb_i][bomb_j] :
            if new_brick[bomb_i][bomb_j] > 1:
                q.append((bomb_i, bomb_j, new_brick[bomb_i][bomb_j]))
            new_brick[bomb_i][bomb_j] = 0
            break

    while q:
        y, x, bn = q.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for k in range(1, bn):
                ny = y + dy*k
                nx = x + dx*k
                if 0 <= ny < h and 0 <= nx < w:
                    if new_brick[ny][nx] > 1:
                        q.append((ny, nx, new_brick[ny][nx]))
                    new_brick[ny][nx] = 0

    return new_brick


def gravity(gravity_brick):
    new_brick = deepcopy(gravity_brick)
    for g_i in range(h-2, -1, -1):
        for g_j in range(w):
            if new_brick[g_i][g_j] and new_brick[g_i+1][g_j] == 0:
                ny = 0
                flag = 0
                for k in range(g_i+1, h):
                    ny = k
                    if new_brick[k][g_j]:
                        flag = 1
                        break
                if flag:
                    new_brick[ny-1][g_j] = new_brick[g_i][g_j]
                else:
                    new_brick[ny][g_j] = new_brick[g_i][g_j]
                new_brick[g_i][g_j] = 0
    return new_brick


def solve(cnt, my_brick):
    global answer
    if cnt == n:
        brick_cnt = 0
        for i in range(h):
            for j in range(w):
                if my_brick[i][j]:
                    brick_cnt += 1
        answer = min(brick_cnt, answer)
        return

    for i in range(w):
        new_brick = bomb(my_brick, i)
        new_brick = gravity(new_brick)
        solve(cnt+1, new_brick)


for tc in range(1, int(input())+1):
    n, w, h = map(int, input().split())
    brick = [list(map(int, input().split())) for _ in range(h)]
    answer = w*h + 1
    solve(0, brick)
    print('#{} {}'.format(tc, answer))