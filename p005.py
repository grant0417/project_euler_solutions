def dividable_up_to(n, div):
    for i in range(div, 1, -1):
        if(n % i != 0):
            return False
    return True

i = 20

while not dividable_up_to(i, 20):
    i += 20

print(i)