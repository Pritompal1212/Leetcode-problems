def countBits(n):
    ans = []
    for i in range(n + 1):
        count = 0
        num = i
        while num > 0:
            count += num & 1  # Check the last bit
            num = num >> 1    # Update num by shifting it right
        ans.append(count)  # Append the count for current i
    return ans

# Test cases
print(countBits(5))   # Output: [0, 1, 1, 2, 1, 2]
print(countBits(2))   # Output: [0, 1, 1]
print(countBits(10))  # Output: [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]
