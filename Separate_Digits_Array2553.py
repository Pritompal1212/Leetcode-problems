def separateDigits(nums):
    result = []
    for num in nums:
        result.extend([int(digit) for digit in str(num)])  # Convert to string and extract digits
    return result

# Example Usage
print(separateDigits([10921, 45, 3]))  # Output: [1, 0, 9, 2, 1, 4, 5, 3]
print(separateDigits([123, 456, 789])) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
