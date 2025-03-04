def maxProduct(nums: list) -> int:
    first, second = 0, 0
    
    for num in nums:
        if num > first:
            first, second = num, first
        elif num > second:
            second = num
            
    return (first - 1) * (second - 1)

# Example usage
print(maxProduct([3, 4, 5, 2]))  # Output: 12
