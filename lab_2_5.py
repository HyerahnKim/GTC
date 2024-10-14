# Function to find the next lexicographic permutation
def next_permutation(perm):
    # Find the largest index k such that perm[k] < perm[k + 1]
    k = -1
    for i in range(len(perm) - 1):
        if perm[i] < perm[i + 1]:
            k = i
    if k == -1:
        return None  # Already the last permutation

    # Find the largest index l such that perm[k] < perm[l]
    l = -1
    for i in range(k + 1, len(perm)):
        if perm[k] < perm[i]:
            l = i
    # Swap perm[k] and perm[l]
    perm[k], perm[l] = perm[l], perm[k]
    # Reverse the sequence from perm[k + 1] to the end
    perm = perm[:k + 1] + perm[k + 1:][::-1]
    return perm


# Function to find the previous lexicographic permutation
def prev_permutation(perm):
    # Find the largest index k such that perm[k] > perm[k + 1]
    k = -1
    for i in range(len(perm) - 1):
        if perm[i] > perm[i + 1]:
            k = i
    if k == -1:
        return None  # Already the first permutation

    # Find the largest index l such that perm[k] > perm[l]
    l = -1
    for i in range(k + 1, len(perm)):
        if perm[k] > perm[i]:
            l = i
    # Swap perm[k] and perm[l]
    perm[k], perm[l] = perm[l], perm[k]
    # Reverse the sequence from perm[k + 1] to the end
    perm = perm[:k + 1] + perm[k + 1:][::-1]
    return perm

n = int(input("Enter n: "))
perm = list(map(int, input(f"Enter the permutation of {n} numbers with space between numbers: ").split()))
next_perm = next_permutation(perm[:])  # Use a copy of the list
prev_perm = prev_permutation(perm[:])  # Use a copy of the list




if next_perm:
    print("Next permutation:", next_perm)
else:
    print("This is the last permutation in lexicographic order.")

if prev_perm:
    print("Previous permutation:", prev_perm)
else:
    print("This is the first permutation in lexicographic order.")
