def isPowerOfFour(n):
    i = 0
    while 4 ** i <= n:
        if 4 ** i == n:
            return True
        i += 1
    return False

# Test the function
print(isPowerOfFour(16))  # Output: True, since 16 is 4^2
print(isPowerOfFour(5))   # Output: False, since 5 is not a power of 4
