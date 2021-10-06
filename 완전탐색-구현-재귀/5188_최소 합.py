dy = [1, 0]
dx = [0, 1]


def min_sum(a, b, my_sum):
    global answer
    if my_sum > answer:
        return

    if a == n-1 and b == n-1:
        answer = min(my_sum, answer)

    for i in range(2):
        ny = a + dy[i]
        nx = b + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            min_sum(ny, nx, my_sum+maps[ny][nx])


for tc in range(1, int(input())+1):
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    answer = 9**10
    min_sum(0,0,maps[0][0])
    print('#{} {}'.format(tc, answer))