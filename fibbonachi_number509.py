def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test cases
print(fibonacci_iterative(0))  # Should print 0
print(fibonacci_iterative(1))  # Should print 1
print(fibonacci_iterative(10))  # Should print 55
