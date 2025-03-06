def signFunc(x: int) -> int:
    return 1 if x > 0 else -1 if x < 0 else 0

def arraySign(nums: list) -> int:
    product_sign = 1
    for num in nums:
        if num == 0:
            return 0
        if num < 0:
            product_sign *= -1
    return product_sign

# Example usage
print(arraySign([-1,-2,-3,-4,3,2,1]))  # Output: 1
