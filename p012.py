def number_of_divisors(n):
    total = 0
    sqrt = int(n ** 0.5)
    for factor in range(1, sqrt + 1):
        if n % factor == 0:
            total += 2
    if sqrt ** 2 == n:
        total -= 1
    return total


i = 1
tri = 0
while True:
    tri += i
    if number_of_divisors(tri) > 500:
        break
    i += 1

print(tri)
