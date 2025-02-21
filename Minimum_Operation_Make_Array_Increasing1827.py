def minOperations(nums):
    operations = 0  # Counter for operations

    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:  # Need to increase
            operations += (nums[i - 1] - nums[i] + 1)
            nums[i] = nums[i - 1] + 1  # Make it strictly increasing

    return operations

# Example Usage
nums = [1, 1, 1]
print(minOperations(nums))  # Output: 3

nums = [1, 5, 2, 4, 1]
print(minOperations(nums))  # Output: 14
