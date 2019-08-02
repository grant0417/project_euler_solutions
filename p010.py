from utils import is_prime

total = 0
n = 1

while n < 2000000:
    n += 1
    if is_prime(n):
        total += n

print(total)
