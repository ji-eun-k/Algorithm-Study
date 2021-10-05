# 거리가 가까운 물고기 많다면 가장 위, 왼쪽에 있는 물고기 먹기
import sys
input = sys.stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]




n = int(input())
# 1, 2, 3, 4, 5, 6 : 물고기 크기
# 9 아기 상어 위치
maps = [list(map(int, input().split())) for _ in range(n)]
baby_shark = 2