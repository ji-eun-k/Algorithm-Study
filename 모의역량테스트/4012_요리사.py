def cal(my_list):
    score = 0
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            score += s[my_list[i]][my_list[j]] + s[my_list[j]][my_list[i]]
    return score


def cook(cnt, k):
    global min_value
    if cnt == n//2:
        a_list = []
        b_list = []
        for j in range(n):
            if visited[j]:
                a_list.append(j)
            else:
                b_list.append(j)
        min_value = min(abs(cal(a_list) - cal(b_list)), min_value)
        return

    for i in range(k, n):
        visited[i] = 1
        cook(cnt+1, i+1)
        visited[i] = 0


for tc in range(1, int(input())+1):
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    visited = [0]*n
    min_value = 0xffffff
    cook(0, 0)
    print('#{} {}'.format(tc, min_value))