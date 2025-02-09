def largestNumber(nums):
    # Convert all numbers to strings
    nums = [str(num) for num in nums]

    # Custom sorting function (Bubble Sort for no imports)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] < nums[j] + nums[i]:
                nums[i], nums[j] = nums[j], nums[i]  # Swap to maintain order

    # Join sorted numbers into a single string
    result = "".join(nums)

    # Handle case where leading zeros exist (e.g., [0, 0] -> "0")
    return result if result[0] != "0" else "0"

print(largestNumber([10, 2]))  
# Output: "210"

print(largestNumber([3, 30, 34, 5, 9]))  
# Output: "9534330"

print(largestNumber([0, 0]))  
# Output: "0"
