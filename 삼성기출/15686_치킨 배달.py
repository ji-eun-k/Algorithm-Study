import sys
input = sys.stdin.readline


def comb(start, my_set:set):
    global ans
    if len(my_set) == m:
        dist = [n*n+1] * h_len
        for t_y, t_x in my_set:
            for idx in range(h_len):
                dist[idx] = min(dist[idx], abs(t_y - house[idx][0]) + abs(t_x - house[idx][1]))
        ans = min(ans, sum(dist))
        return

    for num in range(start, c_len):
        comb(num+1, my_set | {chicken[num]})  # 합집합으로 combination 넘겨줌


n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
chicken = []
house = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        if city[i][j] == 2:
            chicken.append((i, j))

c_len = len(chicken)
h_len = len(house)
ans = float('inf')
comb(0, set())
print(ans)