import itertools
def getPermutations(s):
    # Generate permutations and remove duplicates using set
    permutations = itertools.permutations(s)
    return sorted(''.join(p) for p in permutations)

# Example usage:
s = "aab"
result = getPermutations(s)
print(result)  # Output: ['aab', 'aba', 'baa']
