import math


def permutation_from_rank(n, r):
    elements = list(range(1, n + 1))
    perm = []
    for i in range(n):
        fact = math.factorial(n - 1 - i)
        index = r // fact
        perm.append(elements.pop(index))
        r %= fact
    return perm


n = int(input("Enter number n"))
r = int(input("Enter rank r between 0 and {}".format(math.factorial(n)-1)))

perm = permutation_from_rank(n, r)
print("The permutation with rank", r, "is:", perm)