
def arrayPairSum(nums):
        # Sort the array
    nums.sort()
        # Take the sum of every second element in the sorted array
    return sum(nums[i] for i in range(0, len(nums), 2))

# Example 1
nums = [1, 4, 3, 2]

print(arrayPairSum(nums))  # Output: 4 (Pairs are (1, 2) and (3, 4))

# Example 2
nums = [6, 2, 6, 5, 1, 2]
print(arrayPairSum(nums))  # Output: 9 (Pairs are (1, 2), (2, 5), and (6, 6))

