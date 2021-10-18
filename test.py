# def quick_sort(arr, start, end):
#     if start >= end:
#         return
#
#     l = start + 1
#     r = end
#     pivot = start
#
#     while l <= r:
#         while l <= end and arr[pivot] > arr[l] :
#             l += 1
#
#         while r > start and arr[pivot] < arr[r]:
#             r -= 1
#
#         if l > r:
#             arr[pivot], arr[r] = arr[r], arr[pivot]
#         else:
#             arr[l], arr[r] = arr[r], arr[l]
#
#     quick_sort(arr, start, r-1)
#     quick_sort(arr, r+1, end)


# def merge_sort(arr):
#     if len(arr) == 1:
#         return arr
#
#     l_arr = merge_sort(arr[:len(arr)//2])
#     r_arr = merge_sort(arr[len(arr)//2:])
#
#     new_arr = [0]*len(arr)
#     l_idx, r_idx, k = 0, 0, 0
#     while r_idx < len(r_arr) and l_idx < len(l_arr):
#         if l_arr[l_idx] > r_arr[r_idx]:
#             new_arr[k] = r_arr[r_idx]
#             k += 1
#             r_idx += 1
#         else:
#             new_arr[k] = l_arr[l_idx]
#             l_idx += 1
#             k += 1
#
#     while r_idx < len(r_arr):
#         new_arr[k] = r_arr[r_idx]
#         k += 1
#         r_idx += 1
#
#     while l_idx < len(l_arr):
#         new_arr[k] = l_arr[l_idx]
#         k += 1
#         l_idx += 1
#
#     return new_arr


# my_list = [9, 4, 3, 2, 1, 6, 5]
# # quick_sort(my_list, 0, len(my_list)-1)
# print(merge_sort(my_list))

# 이분 탐색 : sort 먼저 해야함!


def binary(n):
    if n < 2:
        return str(n)
    return binary(n//2) + str(n%2)

print(binary(2))