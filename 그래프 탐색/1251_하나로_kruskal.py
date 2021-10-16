def find_p(x):

    while p[x] != x:
        x = p[x]
    return x


for tc in range(1, int(input())+1):
    n = int(input())
    island = list(zip(list(map(int, input().split())), list(map(int, input().split()))))
    p = [i for i in range(n+1)]
    e = float(input())
    q = []
    for i in range(n):
        for j in range(i, n):
            w = ((island[i][0] - island[j][0])**2 + (island[i][1] - island[j][1])**2)
            q.append((w, i+1, j+1))
    q.sort(key=lambda x:x[0])
    ans = 0
    for i in range(len(q)):
        w, p1, p2 = q[i]
        if find_p(p1) == find_p(p2):
            continue
        else:
            p[find_p(p1)] = find_p(p2)
            ans += w

    print('#{} {}'.format(tc, round(ans*e)))
