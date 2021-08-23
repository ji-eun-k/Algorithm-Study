import sys
input = sys.stdin.readline

# 가장 긴 점 찾고 -> 이 점 기준으로 다시 탐색! -> 다시 풀기

def cal_tree(start: int, cnt:int):
    global tree
    global max_tree
    global visited
    for now_tree in tree[start]:
        if not visited[now_tree[0]]:
            visited[now_tree[0]] = 1
            cal_tree(now_tree[0], now_tree[1]+cnt)

    max_tree = max(max_tree, cnt)


N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, weight = map(int, input().split())
    tree[a].append([b, weight])
    tree[b].append([a, weight])


max_tree = 0
for i in range(1, N):
    if len(tree[i]) == 1:
        visited = [0]*(N+1)
        visited[i] = 1
        cal_tree(i, 0)

print(max_tree)
