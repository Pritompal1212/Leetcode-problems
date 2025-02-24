
def isMonotonic(nums):
    increasing = decreasing = True
        
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:  # Not decreasing
            decreasing = False
        if nums[i] < nums[i - 1]:  # Not increasing
            increasing = False
        
    return increasing or decreasing

nums = [1,2,2,3]
print(isMonotonic(nums))
