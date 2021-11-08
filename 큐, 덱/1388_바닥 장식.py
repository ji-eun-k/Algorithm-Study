N, M = map(int, input().split())
room = [list(input()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        if room[i][j] == '-':
            for k in range(j, M):
                if room[i][k] != '-':
                    break
                room[i][k] = 'X'
            ans += 1
        elif room[i][j] == '|':
            for k in range(i, N):
                if room[k][j] != '|':
                    break
                room[k][j] = 'X'
            ans += 1

print(ans)
