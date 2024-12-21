def kthFactor(n, k):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    
    if len(factors) >= k:
        return factors[k - 1]
    return -1

# Example Usage
print(kthFactor(12, 3))  # Output: 3
print(kthFactor(7, 2))   # Output: 7
print(kthFactor(4, 4))   # Output: -1
