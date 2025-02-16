def check(nums):
    count = 0
    n = len(nums)
    
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:  # Compare with the next element (circular check)
            count += 1
            if count > 1:
                return False  # More than one descent means it's not a rotated sorted array
    
    return True

# **Example Usage**
print(check([3, 4, 5, 1, 2]))  # Output: True (Rotated)
print(check([2, 1, 3, 4]))  # Output: False (Not sorted before rotation)
print(check([1, 2, 3, 4, 5]))  # Output: True (Already sorted)
print(check([1, 1, 1, 2, 3]))  # Output: True (Duplicates handled)
print(check([3, 3, 1, 3]))  # Output: True
