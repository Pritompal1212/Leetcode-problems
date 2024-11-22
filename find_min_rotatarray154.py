
def findMin(nums): 
    if len(nums) == 1: 
        return nums[0]
        
    l, r = 0, len(nums) - 1
        
        # If array is not rotated at all
    if nums[l] < nums[r]: 
        return nums[l]
        
    while l < r:
        mid = (l + r) // 2
            
        if nums[mid] > nums[r]:
            l = mid + 1
        elif nums[mid] < nums[r]:
            r = mid
        else:
            r -= 1  # Handle duplicates
            
    return nums[l]

nums=[2,2,2,0,1]
print(findMin(nums))