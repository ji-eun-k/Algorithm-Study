def k_check():
    for j in range(W):
        first_char = film[0][j]
        check = 0
        for i in range(D):
            if first_char == film[i][j]:
                check += 1
            else:
                first_char = film[i][j]
                check = 1
            if check >= K:
                break
        if check < K:
            return False
    return True


def solve(cnt, change_idx):
    global min_cnt

    if k_check():
        min_cnt = min(cnt, min_cnt)
        return

    if cnt >= min_cnt:
        return

    for i in range(change_idx+1, D):
        origin_film = film[i][:]
        for j in range(W):
            film[i][j] = 1
        solve(cnt+1, i)

        for j in range(W):
            film[i][j] = 0
        solve(cnt+1, i)

        for j in range(W):
            film[i][j] = origin_film[j]


for tc in range(1, int(input())+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    min_cnt = D+1
    solve(0, -1)
    print('#{} {}'.format(tc, min_cnt))