dy = [1, 1, -1, -1]
dx = [1, -1, -1, 1]


def solve(answer, si, sj, start, dire):
    global max_answer
    if (si, sj) == start:
        max_answer = max(max_answer, answer)
        return
    if si < 0 or sj < 0 or si >= n or sj >= n:
        return

    if desert[maps[si][sj]]: # 이미 먹은 곳곳
        return
    else:
        desert[maps[si][sj]] = 1
        solve(answer+1, si+dy[dire], sj+dx[dire], start, dire)
        if dire+1 < 4:
            solve(answer+1, si+dy[dire+1], sj+dx[dire+1], start, dire+1)
        desert[maps[si][sj]] = 0


for tc in range(1, int(input())+1):
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    desert = [0]*101
    max_answer = -1
    for i in range(n-1):
        for j in range(1, n-1):
            desert[maps[i][j]] = 1
            solve(1, i+1, j+1, (i, j), 0)
            desert[maps[i][j]] = 0
    print('#{} {}'.format(tc, max_answer))