import sys
input = sys.stdin.readline
S, E, Q = input().split()
start = int(S[:2])*100 + int(S[3:])
end = int(E[:2])*100 + int(E[3:])
quiting = int(Q[:2])*100 + int(Q[3:])

check = set()
cnt = 0
while True:
    try:
        clock, nickname = input().split()
        my_clock = int(clock[:2])*100+int(clock[3:])

        if my_clock <= start:
            check.add(nickname)

        if end <= my_clock <= quiting:
            if nickname in check:
                cnt += 1
                check.remove(nickname)
    except:
        break

print(cnt)