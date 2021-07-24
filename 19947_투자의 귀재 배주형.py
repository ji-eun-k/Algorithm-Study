h, y = map(int, input().split())

dp = [0]*(y+1)
dp[0] = h #원금

for i in range(1, y+1):
    dp[i] = max(dp[i], int(dp[i-1]*1.05))

    if i-3 >= 0:
        dp[i] = max(dp[i], int(dp[i-3]*1.2))
    if i-5 >= 0:
        dp[i] = max(dp[i], int(dp[i-5]*1.35))

print(dp[y])