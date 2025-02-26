def hasThreeDivisors(n):
    # Step 1: Check if n is a perfect square
    root = 0
    while root * root < n:
        root += 1
    if root * root != n:
        return False

    # Step 2: Check if root is prime
    if root < 2:
        return False
    for i in range(2, root):
        if root % i == 0:
            return False

    return True

# Example Test Cases
print(hasThreeDivisors(4))   # True (Divisors: {1, 2, 4})
print(hasThreeDivisors(9))   # True (Divisors: {1, 3, 9})
print(hasThreeDivisors(16))  # False (Divisors: {1, 2, 4, 8, 16})
print(hasThreeDivisors(25))  # True (Divisors: {1, 5, 25})
print(hasThreeDivisors(10))  # False (Divisors: {1, 2, 5, 10})
