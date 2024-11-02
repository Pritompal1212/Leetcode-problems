def rotate(nums, k):
    n = len(nums)
    k = k % n  # In case k is greater than the length of nums

    # Step 1: Reverse the entire array
    nums.reverse()

    # Step 2: Reverse the first k elements
    nums[:k] = reversed(nums[:k])

    # Step 3: Reverse the remaining elements
    nums[k:] = reversed(nums[k:])

# Test the function
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)  # Rotate in-place
print(nums)  # Expected output: [5, 6, 7, 1, 2, 3, 4]
