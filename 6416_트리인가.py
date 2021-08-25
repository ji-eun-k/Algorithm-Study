
# 들어 오는 간선이 하나도 없는 단 하나의 노드가 존재 (루트)
# 루트 노드를 제외한 모든 노드들은 단 하나의 들어오는 간선이 존재 -> 부모가 두 개면 안 됨
# 루트에서 모든 노드를 방문할 수 있어야 함
class Node:
    def __init__(self):
        self.parent = None
        self.child = None


end = False
i = 0
while True:
    isTree = True
    i += 1
    arr = []
    graph = {}
    while True:
        arr.extend(map(int, input().split()))
        if arr :
            if arr[-1] == arr[-2] == 0:
                break
            if arr[-1] == arr[-2] == -1:
                end = True
                break
    print(arr)
    if end:
        break
    for idx in range(0, len(arr)-1, 2):
        if arr[idx] in graph.keys():
            graph[arr[idx]].child.append(arr[idx+1])
        else :
            graph[arr[idx]] = Node()
            graph[arr[idx]].child = [arr[idx+1]]
            graph[arr[idx]].parent = [-1]
    print(graph)



