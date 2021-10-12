dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]


def tornado(ti, tj, tr):
    global answer
    if 0<=ti<n and 0<=tj<n:
        sand[ti][tj] += tr
    else:
        answer += tr


n = int(input())
sand = [list(map(int, input().split())) for _ in range(n)]
y = n//2
x = n//2
answer = 0
dire = 0
cnt = 0
turn = 0
move = 1
while True:
    ny = y + dy[dire]
    nx = x + dx[dire]
    if sand[ny][nx]:
        p10 = int((sand[ny][nx] * 0.1))
        p7 = int((sand[ny][nx]*0.07))
        p5 = int((sand[ny][nx]*0.05))
        p2 = int((sand[ny][nx]*0.02))
        p1 = int((sand[ny][nx]*0.01))
        rem = sand[ny][nx] - p5 - 2 * (p10 + p7 + p2 + p1)

        p1y_u, p1x_u = y + dy[(dire+3)%4], x + dx[(dire+3)%4]
        p1y_d, p1x_d = y + dy[(dire+1)%4], x + dx[(dire+1)%4]


    if ny == 0 and nx == 0:
        break

    sand[ny][nx] = 0
    y, x = ny, nx
    cnt += 1
    if cnt == move:
        dire = (dire+1)%4
        cnt = 0
        turn += 1
        if turn % 2 == 0:
            move += 1
            turn = 0

print(answer)

