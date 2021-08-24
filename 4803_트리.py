def dfs(start):
    
    return True


while True:
    n, m = map(int, input().split())
    if n == m == 0: #탈출
        break
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0]*(n+1)
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            if dfs(i):
                cnt += 1
                print(i, 'wow')
    print(cnt)