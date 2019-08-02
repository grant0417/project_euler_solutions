def check_palindrome(n):
    s = str(n)
    return s == s[::-1]

p = 0

for x in range(1000):
    for y in range(1000):
        mul = x * y
        if(check_palindrome(mul)):
            if(mul > p):
                p = mul


print(p)