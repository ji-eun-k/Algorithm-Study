import sys

def 
input = sys.stdin.readline
N = int(input())
tree = {}
for _ in range(N):
    a, b, c = input().split()
    tree[a] = [b, c]
