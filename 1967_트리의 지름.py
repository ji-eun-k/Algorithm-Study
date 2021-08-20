import sys
input = sys.stdin.readline
#다시 짜기 가장먼곳 찾고, 그 먼곳에서 다시 돌리기임!!

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
