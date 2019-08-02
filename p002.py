def fib(n):
    if(n > 1):
        return fib(n - 1) + fib(n - 2)
    else:
        return 1

f = 0
i = 1
sum = 0

while(f < 4000000):
    f = fib(i)
    sum += (f if f % 2 == 0 else 0)
    i += 1

print(sum)