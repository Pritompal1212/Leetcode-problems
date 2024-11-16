def searchRange(nums, target):
    st=-1
    en=-1
    for i in range(len(nums)):
        if nums[i]==target:
            if st == -1:
                st = i
            en = i
    
    return [st,en]
        
    
nums = [5,7,7,8,8,10]
target = 1
#     Output: [3,4]
print(searchRange(nums, target))