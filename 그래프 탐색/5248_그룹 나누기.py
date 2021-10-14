def find_p(x):
    if x == p[x]:
        return x
    else:
        return find_p(p[x])


def union(x1, x2):
    p1 = find_p(x1)
    p2 = find_p(x2)
    if p1 == p2:
        return
    else:
        p[p1] = p2


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    p = [i for i in range(n+1)]
    data = list(map(int, input().split()))
    for i in range(m):
        union(data[i*2], data[i*2+1])

    answer = 0
    for i in range(1, n+1):
        if i == p[i]:
            answer += 1

    print('#{} {}'.format(tc, answer))
