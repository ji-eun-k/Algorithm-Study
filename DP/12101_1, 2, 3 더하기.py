def btk(sum_num, check):
    global cnt
    if sum_num > n :
        return
    if n == sum_num :
        cnt += 1
        if cnt == k :
            print('+'.join(check))
            exit(0)

    for i in range(1, 4):
        check.append(str(i))
        btk(sum_num + i, check)
        check.pop()


n, k = map(int, input().split())
cnt = 0
btk(0, [])
print(-1)