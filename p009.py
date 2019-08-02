import math


def find_triplet(n):
    for a in range(500):
        for b in range(500):
            if math.sqrt(a * a + b * b).is_integer():
                if a + b + math.sqrt(a * a + b * b) == 1000:
                    return a, b, math.sqrt(a * a + b * b)


triplet = find_triplet(1000)
print(int(triplet[0] * triplet[1] * triplet[2]))
