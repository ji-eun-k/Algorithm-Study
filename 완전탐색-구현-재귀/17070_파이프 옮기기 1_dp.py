n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

check_dict = {1:(1, 3), 2:(2, 3), 3:(1, 2, 3)}
pos_dict = {1:(0, 1), 2:(1, 0), 3:(1, 1)}
ans = 0