from collections import deque

def bfs(start):
    q = deque([start])
    team[start] = True
    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if not team[next_node]:
                q.append(next_node)
                team[next_node] = True


for tc in range(1, int(input())+1):
    ans = 0
    n, m = map(int, input().split())
    team = [False]*(n+1)
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    for i in range(1, n+1):
        if not team[i]:
            bfs(i)
            ans += 1

    print('#{} {}'.format(tc, ans))