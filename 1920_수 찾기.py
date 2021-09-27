import sys
input = sys.stdin.readline


def binary_search(find_n):
    s = 0
    e = n-1
    while s <= e:
        mid = (s+e)//2
        if number[mid] == find_n:
            return 1
        elif number[mid] > find_n:
            e = mid - 1
        else :
            s = mid + 1
    return 0


n = int(input())
number = list(map(int, input().rstrip().split()))
number.sort()
m = int(input())
for i in list(map(int, input().rstrip().split())):
    print(binary_search(i))