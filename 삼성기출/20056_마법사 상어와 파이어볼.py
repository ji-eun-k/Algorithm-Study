dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

def move():
    

n, m, k = map(int, input().split())
grid = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    ri, ci, mi, si, di = map(int, input().split())
    grid[ri-1][ci-1].append([mi, si, di])

print(grid)