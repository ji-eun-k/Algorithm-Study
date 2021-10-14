n = 8
stack = [0]*n
top = -1


def push(data):
    global top
    if top == n-1:
        return 'overflow'
    top += 1
    stack[top] = data


def pop():
    global top
    if top == -1 :
        return 'underflow'
    top -= 1
    return stack[top+1]


