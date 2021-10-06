n = int(input())
dp = [[0]*3 for _ in range(n)]
# 0 : 윗칸 모두 빔, 1: 윗칸 왼쪽 채움 2: 윗칸 오른쪽 채움
dp[0][0] = dp[0][1] = dp[0][2] = 1

for i in range(1, n):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2])%9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2])%9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1])%9901

print(sum(dp[n-1])%9901)