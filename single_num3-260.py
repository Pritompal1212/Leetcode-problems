def singleNumber(nums):
    nums.sort()  # Sort the array
    result = []
    
    i = 0
    while i < len(nums) - 1:
        if nums[i] != nums[i + 1]:
            result.append(nums[i])  # Add unique number to the result
            i += 1  # Move to the next element
        else:
            i += 2  # Skip the duplicate pair
    if i == len(nums) - 1:  # If the last element is unique
        result.append(nums[i])
    
    return result

# Test case
nums = [1, 2, 1, 3, 2, 5]
print(singleNumber(nums))  # Output: [3, 5] or [5, 3]

