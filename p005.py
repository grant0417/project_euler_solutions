def dividable_up_to(n, div):
    for i in range(div, 1, -1):
        if n % i != 0:
            return False
    return True


n = 20

while not dividable_up_to(n, 20):
    n += 20

print(n)
