def largest_division(n):
    d = 2
    while n > 1:
        if n % d == 0:
            n /= d
        else:
            d += 1
    return d

print(largest_division(600851475143))