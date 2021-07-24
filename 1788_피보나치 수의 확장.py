n = int(input())
fib = [0, 1]

flag = 0

if n < 0 :
    if abs(n) % 2 == 0 :
        flag = -1
    else :
        flag = 1
elif n > 0 :
    flag = 1


for i in range(2, abs(n)+1):
    fib.append((fib[i-1] + fib[i-2])% 1000000000)

print(flag)
print(fib[abs(n)])