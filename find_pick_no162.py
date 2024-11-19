def findPeakElement(nums):
    large=0
    for i in range(len(nums)):
        if nums[i]>nums[large]:
            large=i
    return large
nums = [1,2,3,1]
print(findPeakElement(nums))