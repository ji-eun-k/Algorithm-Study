for tc in range(1, int(input())+1):
    n = int(input())
    times = [list(map(int, input().split())) for _ in range(n)]
    times.sort(key=lambda x:(x[1], x[0]))
    answer = 1
    end_time = times[0][1]
    for time in times:
        if end_time <= time[0]:
            answer += 1
            end_time = time[1]
    print('#{} {}'.format(tc, answer))