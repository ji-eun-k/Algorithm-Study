for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort(reverse=True)
    trucks.sort(reverse=True)
    answer = 0
    idx = 0
    for truck in trucks:
        while idx < len(containers):
            if containers[idx] <= truck :
                answer += containers[idx]
                idx += 1
                break
            else:
                idx += 1
    print('#{} {}'.format(tc, answer))

