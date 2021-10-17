from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n = int(input())
adj = defaultdict(deque)
team = [0 for _ in range(n+1)]

for _ in range(n-2):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)


q = deque([1])
ans = [1]
while q:
    x = q.popleft()
    team[x] = 1
    for i in adj[x]:
        if not team[i]:
            q.append(i)

for i in range(1, n+1):
    if not team[i]:
        ans.append(i)
        break

print(*ans)