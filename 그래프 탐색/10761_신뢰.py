for tc in range(1, int(input())+1):
    data = input().split()
    n = int(data[0])
    order = data[1:]
    time = 0
    orange_pos = 1
    blue_pos = 1
    for i in range(n):
        robot, button = order[i*2], order[i*2+1]