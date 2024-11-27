def move_zeros(nums):
    # Pointer for the position of the next non-zero element
    non_zero_index = 0

    # Traverse through the array
    for i in range(len(nums)):
        if nums[i] != 0:
            # Swap the current element with the element at non_zero_index
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1

    return nums

# Example usage
nums = [0, 1, 0, 3, 12]
print(f"Original array: {nums}")
result = move_zeros(nums)
print(f"Array after moving zeros: {result}")
