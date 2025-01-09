def sortArrayByParity(nums):
    even = []  # List to store even numbers
    odd = []   # List to store odd numbers
    
    for num in nums:
        if num % 2 == 0:
            even.append(num)  # Add to even list
        else:
            odd.append(num)   # Add to odd list
    
    return even + odd  # Combine even and odd lists

# Test cases
print(sortArrayByParity([3, 1, 2, 4]))  # Output: [2, 4, 3, 1] or [4, 2, 1, 3]
print(sortArrayByParity([0, 1]))        # Output: [0, 1]
