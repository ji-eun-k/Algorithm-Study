def tsp(start, now, cnt, cost):
    global min_cost

    if cnt == n:
        if city[now][start]:
            min_cost = min(min_cost, cost+city[now][start])

    for i in range(n):
        if i != start and city[now][i] != 0 and visited[i] == False:
            visited[i] = True
            tsp(start, i, cnt+1, cost+city[now][i])
            visited[i] = False


for tc in range(1, int(input())+1):
    n = int(input())
    city = [list(map(int, input().split())) for _ in range(n)]
    visited = [False]*(n+1)
    visited[0] = True
    min_cost = 9**10
    tsp(0, 0, 1, 0)
    print('#{} {}'.format(tc, min_cost))
