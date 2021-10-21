import sys
input = sys.stdin.readline
from copy import deepcopy

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]


def shark_move(shark_y, shark_x, shark_d, eat_fish, fish_map):
    global ans, maps, fish
    new_maps = deepcopy(fish_map)
    print(new_maps)
    fish_move(shark_y, shark_x, new_maps)
    print(new_maps)


def fish_move(sy, sx, fish_map):
    for idx in range(16):
        if fish[idx]:
            y, x = fish[idx][0], fish[idx][1]
            fish_d = fish_map[y][x][1]
            for k in range(8):
                new_d = (fish_d + k) % 8
                ny = y + dy[new_d]
                nx = x + dx[new_d]
                if 0 <= ny < 4 and 0 <= nx < 4 and ny != sy and nx != sx:
                    fish_map[y][x][1] = new_d
                    change_fish = fish_map[ny][nx][0]
                    fish_map[y][x][0], fish_map[ny][nx][0] = fish_map[ny][nx][0], fish_map[y][x][0]
                    fish[idx][0], fish[change_fish][0] = fish[change_fish][0], fish[idx][0]
                    fish[idx][1], fish[change_fish][1] = fish[change_fish][1], fish[idx][1]
                    fish_map[ny][nx][1], fish_map[y][x][1] = fish_map[y][x][1], fish_map[ny][nx][1]
                    break





input_data = [list(map(int, input().split())) for _ in range(4)]
maps = [[], [], [], []]
fish = [[] for _ in range(16)]
ans = 0

# 물고기,
for i in range(4):
    for j in range(0, 8, 2):
        maps[i].append([input_data[i][j]-1, input_data[i][j+1]-1])
        fish[input_data[i][j]-1] = [i, j//2]

# 상어가 일단 0,0 물고기 먹음
shark_dir = maps[0][0][1]
first_eat = maps[0][0][0] + 1
fish[first_eat-1], maps[0][0] = [], []

shark_move(0, 0, shark_dir, first_eat, maps)
print(ans)
