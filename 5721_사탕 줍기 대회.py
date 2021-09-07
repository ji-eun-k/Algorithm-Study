while True:
    m, n = map(int, input().split())
    if m == n == 0 :
        break
    else :
        candy = []
        for _ in range(m):
            candy.append(list(map(int, input().split())))

        for i in range(n):

    # # i번째에서 선택할수 있는 최대값
    # dp1[]
    # # 처음부터 i번째행까지 선택할 수 잇는 최대값
    # dp2[i] = max(dp2[i - 2] + dp[i], dp2[i - 1])