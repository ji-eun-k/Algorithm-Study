def find_parent(node):
    parent_list = []
    while True:
        if tree[node][0] == 0 :
            return parent_list
        parent = tree[node][0]
        parent_list.append(parent)
        node = parent


def find_near_node():
    for p1 in node1_parent:
        for p2 in node2_parent:
            if p1 == p2:
                return p1


def find_subtree(node):
    stack = [node]
    cnt = 0
    while stack:
        now_node = stack.pop()
        cnt += 1
        if tree[now_node][1] != 0 :
            stack.append(tree[now_node][1])
        if tree[now_node][2] != 0 :
            stack.append(tree[now_node][2])
    return cnt


for tc in range(1, int(input())+1):
    v, e, node1, node2 = map(int, input().split())
    # 부모, 자식1, 자식2
    tree = [[0, 0, 0] for _ in range(v+1)]
    temp = list(map(int, input().split()))
    for i in range(0, e*2, 2):
        # 부모 - 자식
        tree[temp[i+1]][0] = temp[i]
        if tree[temp[i]][1] == 0:
            tree[temp[i]][1] = temp[i+1]
        else:
            tree[temp[i]][2] = temp[i+1]
    node1_parent = find_parent(node1)
    node2_parent = find_parent(node2)
    near_node = find_near_node()
    print('#{} {} {}'.format(tc, near_node, find_subtree(near_node)))
