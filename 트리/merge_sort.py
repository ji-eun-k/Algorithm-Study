def merge_sort(arr):
    global answer
    if len(arr) == 1:
        return arr
    left = merge_sort(arr[:len(arr)//2])
    right = merge_sort(arr[len(arr)//2:])

    if left[-1] > right[-1]:
        answer += 1

    i, j, k = 0, 0, 0
    new_arr = [0]*(len(left)+len(right))
    while True:
        if i >= len(left) or j >= len(right):
            break
        if left[i] <= right[j]:
            new_arr[k] = left[i]
            k+=1
            i+=1
        elif left[i] > right[j]:
            new_arr[k] = right[j]
            j+=1
            k+=1
    if j>= len(right):
        while i < len(left):
            new_arr[k] = left[i]
            i += 1
            k += 1
    elif i>= len(left):
        while j < len(right):
            new_arr[k] = right[j]
            j += 1
            k += 1
    return new_arr


for tc in range(1, int(input())+1):
    n = int(input())
    input_arr = list(map(int, input().split()))
    answer = 0
    answer_arr = merge_sort(input_arr)
    print('#{} {} {}'.format(tc, answer_arr[n//2], answer))
