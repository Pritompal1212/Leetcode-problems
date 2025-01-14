def search(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) // 2  # Use integer division to get the midpoint index
        if nums[m] == target:
            return m  # Return the index if target is found
        elif nums[m] > target:
            r = m - 1  # Move the right pointer to the left of mid
        else:
            l = m + 1  # Move the left pointer to the right of mid

    return -1  # Return -1 if the target is not found
nums = [-1,0,3,5,9,12]
target = 9
print(search(nums, target))