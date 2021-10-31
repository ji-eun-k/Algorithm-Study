data = list(input())
answer = 0
num = {'H':1, 'C':12, 'O':16}
stack = []
# 스택에 괄호 집어 넣고 빼고 ?? 숫자 몇개인지도 같이넣고
# 만약에 숫자 없으면 ?..

i = len(data) - 1
while i >= 0:
    print(stack)
    temp = data[i]
    if temp.isdecimal():
        stack.append(int(temp))
    elif temp == ')':
        if stack and int == type(stack[-1]):
            stack.append(temp)
            i -= 1
            continue

        stack.append(1)
        stack.append(temp)

    elif temp == '(':
        temp_sum = 0
        while True:
            temp2 = stack.pop()
            if temp2 == ')':
                answer += temp_sum * stack.pop()
                break
            if type(stack[-1]) == int:
                temp_sum += num[temp2] * stack.pop()

            else:
                temp_sum += num[temp2]
    else:
        stack.append(temp)
    i -= 1

while stack:
    a = stack.pop()

    if stack and type(stack[-1]) == int:
        answer += num[a] * stack.pop()
    else:
        answer += num[a]


print(answer)
