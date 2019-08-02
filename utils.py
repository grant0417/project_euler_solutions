def is_prime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def divisors(n): 
    sum = 0
    i = 1
    while i <= n: 
        if (n % i==0): 
            sum += 1
        i = i + 1
    return sum
