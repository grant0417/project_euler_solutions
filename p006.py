def sum_of_squares(l):
    s = []
    for i in l:
        s.append(i ** 2)
    return sum(s)

def square_of_sum(l):
    return sum(l) ** 2

l = list(range(1, 101))
print(square_of_sum(l) - sum_of_squares(l))