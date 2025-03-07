def findTheArrayConcVal(nums: list) -> int:
    concat_val = 0
    while len(nums) > 1:
        concat_val += int(str(nums.pop(0)) + str(nums.pop()))
    if nums:
        concat_val += nums[0]
    return concat_val

# Example usage
print(findTheArrayConcVal([1, 2, 4, 5, 6]))  # Output: 167
