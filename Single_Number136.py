# def singleNumber(nums):
#     arr=[]
#     st=0
#     en=st+1
#     for i in range(len(nums)):
#         if nums[st]==nums[en]:
#             a=arr.append(st,en)
#             return a
#     return nums

# nums=[2,2,1]
# r=singleNumber(nums) 
# print(r)       




def removeElement(nums, val):
    arr=[]
    for i in nums:
        if i!=val:
            arr.append(i)
    return arr

nums=[2,2,1]
val=2
print(removeElement(nums, val))