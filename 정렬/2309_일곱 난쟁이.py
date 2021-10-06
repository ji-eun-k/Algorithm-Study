nan = []
for i in range(9):
    nan.append(int(input()))

sum_nan = sum(nan)
ans = []

for i in range(8):
    for j in range(i+1, 9):
        if sum_nan - nan[i] - nan[j] == 100:
            num1, num2 = nan[i], nan[j]
            nan.remove(num1)
            nan.remove(num2)
            nan.sort()

            break
    if len(nan) <9:
        break

for i in nan:
    print(i)