#Write a program which reads a permutation of {1, . . . , n} and it displays the rank of that permutation.

import math

def rank_of_permutation(perm):
    n = len(perm)
    elements = list(range(1, n + 1))
    rank = 0
    for i in range(n):
        index = elements.index(perm[i])
        rank += index * math.factorial(n - 1 - i)
        elements.pop(index)
    return rank

n = int(input("Enter n: "))
perm = list(map(int, input(f"Enter the permutation of {n} numbers with space between numbers ").split()))
rank = rank_of_permutation(perm)
print("The rank of the permutation is:", rank)