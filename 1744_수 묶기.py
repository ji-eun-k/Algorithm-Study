import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

idx = 0
answer = 0
while True:
    if idx <= n-2:
        if arr[idx] > 1 and arr[idx+1] > 1:
            answer += arr[idx] * arr[idx+1]
            idx += 2
        elif arr[idx] <= 1:
            answer += arr[idx]
            idx += 1
        