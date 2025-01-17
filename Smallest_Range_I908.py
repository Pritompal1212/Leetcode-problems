def minimumScore(nums, k):
    min_num = min(nums)
    max_num = max(nums)
    # Calculate new range after applying operations
    new_min = min_num + k
    new_max = max_num - k
    # The minimum score is the difference between new_max and new_min
    return max(0, new_max - new_min)

# Example 1
nums = [1, 3, 6]
k = 3
print(minimumScore(nums, k))  # Output: 0

# Example 2
nums = [4, 7, 10, 14]
k = 2
print(minimumScore(nums, k))  # Output: 6

# Example 3
nums = [8, 10, 14]
k = 5
print(minimumScore(nums, k))  # Output: 0
