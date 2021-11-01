chemi = {'H': 1, 'C': 12, 'O': 16}
data = input()
idx = 0
stack = []

# 덧셈 + 괄호 있는 계산기 로직과 비슷함
while idx < len(data):
    # 여는 괄호일 경우 일단 stack에 집어 넣음
    if data[idx] == '(':
        stack.append('(')
    # 닫는 괄호일 경우
    elif data[idx] == ')':
        # 여는 괄호가 나올 때 까지 pop 해주며 temp_sum에 저장
        temp_sum = 0
        while True:
            temp = stack.pop()
            if temp == '(':
                stack.append(temp_sum)
                break
            temp_sum += temp
        # 만약 여는 괄호 뒤에 숫자가 있으면 stack top에 저장된 괄호 안의 연산 값에 곱하기
        if idx + 1 < len(data) and data[idx+1].isdecimal():
            idx += 1
            stack.append(stack.pop()*int(data[idx]))
    # 만약 숫자일 경우 바로 앞에 있는 원소에 곱해줌
    elif data[idx].isdecimal():
        stack.append(stack.pop()*int(data[idx]))
    # 원소일 경우 숫자로 바꿔줌
    else:
        stack.append(chemi[data[idx]])
    idx += 1

print(sum(stack))
