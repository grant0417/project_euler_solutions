from utils import is_prime

sum = 0
n = 1

while n < 2000000:
    n += 1
    if(is_prime(n)):
        sum += n
    

print(sum)