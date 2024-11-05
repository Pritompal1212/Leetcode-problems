def singleNumber(nums):
    #nums.sort()
    for i in range(len(nums)):
        if nums[i] not in nums[i+1:] and nums[i] not in nums[:i]:
            return nums[i]
        
nums=[2,2,3,2]
print(singleNumber(nums))


#we can use dictionary

def singleNumber(nums):
        
    d={}
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for key, val in d.items():
        if d[key]==1:
            return key
nums=[2,2,3,2]
print(singleNumber(nums))



#and also using bit manuplition
def singleNumber(nums):
    # Initialize variables to store bits appearing once and twice
    ones, twos = 0, 0

    for num in nums:
        # Update 'ones' and 'twos' with the current number
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones

    return ones

# Test the function
nums = [2, 2, 3, 2]
print(singleNumber(nums))  # Output should be 3
