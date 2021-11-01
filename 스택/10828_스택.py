import sys
input = sys.stdin.readline
stack = []

for _ in range(int(input())):
    data = input().split()
    # push면 stack에 추가
    if data[0] == 'push':
        stack.append(data[1])
    # stack이 존재하면 top 출력 아니면 -1
    elif data[0] == 'top':
        print(stack[-1] if stack else -1)
    # stack 길이 출력
    elif data[0] == 'size':
        print(len(stack))
    # 스택이 있으면 0 아니면 1
    elif data[0] == 'empty':
        print(0 if stack else 1)
    # 스택이 있으면 pop 아니면 -1
    elif data[0] == 'pop':
        print(stack.pop() if stack else -1)