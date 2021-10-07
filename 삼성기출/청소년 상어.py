dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
input_data = [list(map(int, input().split())) for _ in range(4)]
maps = [[], [], [], []]

# 물고기,
for i in range(4):
    for j in range(0, 8, 2):
        maps[i].append((input_data[i][j], input_data[i][j+1]))

print(maps)