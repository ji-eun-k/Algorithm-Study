import sys
input = sys.stdin.readline

n, k = map(int, input().split()) #물품의 수 n, 버틸수 있는 무게 k

items = [list(map(int, input().split())) for _ in range(n)]

# dp에 가치합 저장, dp[물건인덱스][가방무게]
knapsack = [[0]*(k+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        # 현재 확인할 물건
        now_weight = items[i-1][0]
        now_value = items[i-1][1]

        if j < now_weight :
            knapsack[i][j] = knapsack[i-1][j]
        else :
            knapsack[i][j] = max(knapsack[i-1][j], knapsack[i-1][j-now_weight] + now_value)

print(knapsack[n][k])
