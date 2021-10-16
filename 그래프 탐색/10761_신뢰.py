for tc in range(1, int(input())+1):
    data = input().split()
    n = int(data[0])
    order = data[1:]
    time = 0
    orange_pos = 1
    orange_time = 0
    blue_pos = 1
    blue_time = 0
    for i in range(n):
        # print('O : {} {}/ B: {} {}'.format(orange_pos, orange_time, blue_pos, blue_time))
        robot, button = order[i*2], int(order[i*2+1])
        if robot == 'B':
            if time == blue_time:
                blue_time += abs(blue_pos - button) + 1
                blue_pos = button
                time = blue_time
            else:
                if time - blue_time > abs(blue_pos - button):
                    time += 1
                    blue_time = time
                    blue_pose = button
                else:
                    time += abs(blue_pos - button) - (time-blue_time) + 1
                    blue_pos = button
                    blue_time = time

        else:
            if time == orange_time:
                orange_time += abs(orange_pos - button) + 1
                time = orange_time
                orange_pos = button
            else:
                if time - orange_time > abs(orange_pos - button):
                    time += 1
                    orange_time = time
                    orange_pos = button
                else:
                    time += abs(orange_pos-button) - (time-orange_time) + 1
                    orange_pos = button
                    orange_time = time

    print('#{} {}'.format(tc, time))