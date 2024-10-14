
sequence = [1, 2, 3, 4]
n = len(sequence)

# Generate the permutation list {1, 2, ..., n}
permutation = list(range(1, n + 1))

# Check if the input sequence matches the expected sequence
if sequence == permutation:
    print("a permutation")
else:
    print("not a permutation")