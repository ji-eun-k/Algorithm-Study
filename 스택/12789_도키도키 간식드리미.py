N = int(input())
num = 1
# 원래 줄
stack = list(map(int, input().split()))[::-1]
# 한명씩 설 수 있는 공간
new_stack = []

while stack or new_stack:
    # 만약 한명씩 설 수 있는 공간에 사람이 있고, 맨 앞 사람이 지금 나와야하는 num과 같으면 pop, num ++
    if new_stack and new_stack[-1] == num:
        new_stack.pop()
        num += 1
        continue
    # 한 명씩 설수 있는 공간에 아무도 없거나 맨 앞사람이 지금 나와야하는 번호가 아니면 줄 서 있는 곳에서 일단 한명 pop
    student = stack.pop()
    # 만약 지금 pop한 애가 맞는 순서라면
    if student == num:
        num += 1
        continue
    # 만약 한명씩 설 수 있는 공간에 사람이 있고, 그 사람의 순서보다 지금 pop한 애 순서가 더 클 경우 무조건 sad
    if new_stack and new_stack[-1] < student:
        print('Sad')
        break
    # 그게 아니라면 일단 한명씩 줄서는 공간에 student 추가
    new_stack.append(student)
else:
    # break 걸리지 않고 while문 끝나면 nice 출력
    print('Nice')