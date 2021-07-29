import sys
input = sys.stdin.readline

while True:
    words = input().rstrip()
    if words == '.':
        break
    stack = []
    isbal = True

    for word in words:
        if word == '(' or word == '[':
            stack.append(word)

        elif word == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else :
                isbal = False
                break

        elif word ==']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else :
                isbal = False
                break


    if isbal and not stack:
        print('yes')
    else:
        print('no')