n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

check_dict = {0: (0, 2), 1: (1, 2), 2: (0, 1, 2)}
pos_dict = {0: (0, 1), 1: (1, 0), 2: (1, 1)}
ans = 0
dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
for i in range(n):
    for j in range(n):
        for k in range(3):
            if dp[i][j][k] and not house[i][j]:  # 해당 방향으로 파이프가 놓이는 방법이 있고, 벽이 없음
                for x in check_dict[k]:
                    ny = i + pos_dict[x][0]
                    nx = j + pos_dict[x][1]
                    if ny < n and nx < n and not house[ny][nx]:
                        if x != 2: # 대각선이 아니라면
                            dp[ny][nx][x] += dp[i][j][k]
                        else: # 대각선이라면
                            if not house[ny-1][nx] and not house[ny][nx-1]:
                                dp[ny][nx][x] += dp[i][j][k]


print(sum(dp[n-1][n-1]))