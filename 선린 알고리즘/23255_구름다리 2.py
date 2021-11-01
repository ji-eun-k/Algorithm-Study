# 다리 단방향 저장

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
color = [1 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
