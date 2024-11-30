def findDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

# Test case
nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))  # Output: 2
