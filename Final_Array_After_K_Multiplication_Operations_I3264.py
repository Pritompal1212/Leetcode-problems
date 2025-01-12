def modifyArray(nums, k, multiplier):
    for _ in range(k):
        # Find the index of the first minimum value
        min_index = nums.index(min(nums))
        # Replace the minimum value with its product with multiplier
        nums[min_index] *= multiplier
    return nums

# Test cases
print(modifyArray([1, 3, 2, 4], 2, 2))  # Example 1: Output: [2, 3, 2, 4]
print(modifyArray([5, 1, 3, 1], 3, 3))  # Example 2: Output: [5, 9, 3, 3]
print(modifyArray([10, 5, 5], 1, 4))    # Example 3: Output: [10, 20, 5]
