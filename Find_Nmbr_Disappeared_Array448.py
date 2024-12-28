def findDisappearedNumbers(nums):
    n = len(nums)
    full_set = set(range(1, n + 1))  # All numbers from 1 to n
    nums_set = set(nums)  # Unique numbers present in nums
    return list(full_set - nums_set)  # Find the missing numbers

# Example Usage
nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(nums1))  # Output: [5, 6]

nums2 = [1, 1]
print(findDisappearedNumbers(nums2))  # Output: [2]
