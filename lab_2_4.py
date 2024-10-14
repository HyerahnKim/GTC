def inverse_permutation(perm):
    n = len(perm)
    inv = [0] * n
    for i in range(n):
        inv[perm[i] - 1] = i + 1
    return inv

# Example usage
n = int(input("Enter n: "))
perm = list(map(int, input(f"Enter the permutation of {n} numbers with space between numbers").split()))
inv = inverse_permutation(perm)
print(inv)