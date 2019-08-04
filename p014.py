def collatz_chain_length(n):
    i = 0
    while n > 1:
        i += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    return i


longest_chain = 0
digit = 0

for i in range(1000000):
    length = collatz_chain_length(i)
    if length > longest_chain:
        longest_chain = length
        digit = i

print(digit)
