import sys
input = sys.stdin.readline

# 나이트는 무조건 오른쪽으로 이동
dy = [-2, -1, 1, 2]
dx = [1, 2, 2, 1]

n, m = map(int, input().split())
chess = [[0]*m for _ in range(n)]

