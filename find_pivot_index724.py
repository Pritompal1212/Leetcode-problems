
def pivotIndex(nums):
    total_sum = sum(nums)
    left_sum = 0
        
    for i, num in enumerate(nums):
        right_sum = total_sum - left_sum - num
        if left_sum == right_sum:
            return i
            left_sum += num  # Update left sum for next iteration
        
    return -1

nums = [1,7,3,6,5,6]
print(pivotIndex(nums))
