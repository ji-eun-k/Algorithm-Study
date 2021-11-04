import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# 오큰수 초기화
NGE = [-1]*N
stack = deque()
# A 배열 앞에서부터 차례로 돌면서 확인
for i in range(N):
    # stack이 있고 stack top의 첫번째값(수열 A[i-k]의 값)이 A[i]보다 작을 경우, pop 해주면서 오큰수 업데이트
    while stack and (stack[-1][0] < A[i]):
        tmp, idx = stack.pop()
        NGE[idx] = A[i]
    # stack이 없거나, stack top의 첫번째 값이 A[i]보다 클 경우 stack에 추가
    stack.append([A[i], i])

print(*NGE)
