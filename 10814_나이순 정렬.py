import sys
input = sys.stdin.readline
n = int(input())
member = []
for _ in range(n):
    a, b = input().split()
    member.append([int(a), b])

mem = sorted(member, key=lambda x: x[0])
for i in range(n):
    print(*mem[i])