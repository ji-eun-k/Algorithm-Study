import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = int(input())
    method = [[0]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
