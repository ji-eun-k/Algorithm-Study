N = int(input())
arr = list(map(int, input().split()))
delete = int(input())
cnt = 0

arr[delete] = -2  # 주어진 삭제할 노드번호를 먼저 -2 로 변환

for i in range(N):

    if arr[i] != -1 and arr[i] != -2 and arr[arr[i]] == - 2:  # i번째 인덱스를 가진 노드의 값이 -1(루트)가 아니면서 i번째 노드번호가 가진 부모노드가 -2 라면
        arr[i] = -2  # 해당 자식노드인 i번째 노드도 -2 로 같이 변경

for i in range(N):
    if arr[i] != -2 and i not in arr:  # 배열의 i번째 노드가 -2가 아니고 i가 arr에 없다면 리프노드이다.
        cnt += 1

print(cnt)

'''
25
6 2 8 19 22 -1 7 24 23 8 5 24 13 8 12 19 22 10 23 21 10 5 5 10 19
23
'''