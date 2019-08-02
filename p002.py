def fib(n):
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1


f = 0
i = 1
total = 0

while f < 4000000:
    f = fib(i)
    total += (f if f % 2 == 0 else 0)
    i += 1

print(total)
