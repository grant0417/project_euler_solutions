from utils import is_prime

i = 0
n = 1

while i < 10001:
    n += 1
    if(is_prime(n)):
        i += 1
    

print(n)