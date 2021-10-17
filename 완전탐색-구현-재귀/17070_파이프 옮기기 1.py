import sys
input = sys.stdin.readline


def dfs(y, x, pos):
    global ans

    if pos == 1:
        # 가로 이동
        if 0 <= x+1 < n and not house[y][x+1]:
            if y == n - 1 and x+1 == n - 1:
                ans += 1
            else:
                dfs(y, x+1, 1)
        # 대각선 이동
        if y + 1 < n and x + 1 < n and not house[y][x + 1] and not house[y + 1][x + 1] and not house[y + 1][x]:
            if y + 1 == n - 1 and x + 1 == n - 1:
                ans += 1
            else:
                dfs(y + 1, x + 1, 3)

    elif pos == 2:
        # 세로 이동
        if y+1 < n and not house[y+1][x]:
            if y+1 == n-1 and x == n-1:
                ans +=1
            else:
                dfs(y+1, x, 2)
        # 대각선 이동
        if y + 1 < n and x + 1 < n and not house[y][x+1] and not house[y+1][x+1] and not house[y+1][x]:
            if y+1 == n - 1 and x+1 == n - 1:
                ans += 1
            else:
                dfs(y + 1, x + 1, 3)

    elif pos == 3:
        # 세로 이동
        if y+1 < n and not house[y+1][x]:
            if y+1 == n-1 and x == n-1:
                ans +=1
            else:
                dfs(y+1, x, 2)
        # 가로 이동
        if x+1 < n and not house[y][x+1]:
            if y == n - 1 and x+1 == n - 1:
                ans += 1
            else:
                dfs(y, x+1, 1)
        # 대각선 이동
        if y + 1 < n and x + 1 < n and not house[y][x+1] and not house[y+1][x+1] and not house[y+1][x]:
            if y+1 == n - 1 and x+1 == n - 1:
                ans += 1
            else:
                dfs(y + 1, x + 1, 3)


# 1: 가로, 2: 세로, 3: 대각선
n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

ans = 0
dfs(0, 1, 1)
print(ans)
