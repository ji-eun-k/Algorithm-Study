def addn(n)
    if n == 1
        return 1
    elif n == 2
        return 2
    elif n == 3
        return 4
    else 
        return addn(n-1) + addn(n-2) + addn(n-3)

T = int(input())
for _ in range(T)
    print(addn(int(input())))