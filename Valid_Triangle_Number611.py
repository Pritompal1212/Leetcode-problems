def triangleNumber(nums):
    nums.sort()  # Sort the array
    n = len(nums)
    count = 0

    # Iterate for each possible largest side
    for k in range(n - 1, 1, -1):
        i, j = 0, k - 1
        while i < j:
            # Check if nums[i] + nums[j] > nums[k]
            if nums[i] + nums[j] > nums[k]:
                count += (j - i)  # All pairs between i and j are valid
                j -= 1
            else:
                i += 1

    return count

# Test Cases
print(triangleNumber([2, 2, 3, 4]))  # Output: 3
print(triangleNumber([4, 2, 3, 4]))  # Output: 4
print(triangleNumber([1, 1, 1, 1]))  # Output: 4
