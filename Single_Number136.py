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



# def removeElement(nums):
#     s={}
#     for i in nums:
#         if i not in s:
#             s[i]= 1
#         else:
#             s[i]+=1
#     return s
    

# nums=[2,2,1]

# print(removeElement(nums))


#authentic
def removeElement(nums):
    ans=0
    for i in nums:
        ans ^= i
    return ans
    
    
nums=[2,2,1] 
print(removeElement(nums))