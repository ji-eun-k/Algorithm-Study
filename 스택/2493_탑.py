N = int(input())
signal = [0]*N
top = list(map(int, input().split()))
stack = []
for i in range(N-1, -1, -1):
    while stack and top[i] > top[stack[-1]]:
        signal[stack.pop()] = i + 1
    stack.append(i)

print(*signal)
