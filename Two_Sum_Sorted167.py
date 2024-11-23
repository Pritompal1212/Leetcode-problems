def twoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums [j] == target:
                return [i +1 , j +1]  # "i +1" & "j +1" bcz of output should be [1,2] otherwise no need to add 1 
                    
    
nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))

# ================ but time limit pblm here so see new one

def twoSum(nums,target):
    l=0
    r=len(nums)-1
    while l<r:
        total = nums[l] + nums[r]
        if total == target:
            return [l +1 , r +1]
        elif total > target:
            r-=1
        else:
            l+=1
    
nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))