# nums=[0,1,2,2,3,0,4,2]
# val=2
# st=0
# arr=[]

# for item in nums:              # i totkhn colbe jotokhan na i last projonto jay
#     if item!=val:              #  i jodi given value(removeable value) na hoy taile kusi ekta korte hobe
#         arr.append(item)       # i jodi value na hoy taile notun array te rakhte hobe sei notun ta return korte hobe
        
# print(len(arr))


# def removeElement(nums, val):
#     arr=[]
#     for i in nums:
#         if i!=val:
#             arr.append(i)
#     return len(arr)

# nums=[3,2,2,3]
# val=3
# r=removeElement(nums,val)
# print(r)



def removeElement(nums, val):
    arr=[]
    for i in nums:
        if i!=val:
            arr.append(i)
    return arr

nums=[3,2,2,3]
val=3
print(removeElement(nums, val))




#also use this program -> leetcode accept it 

# class Solution(object):
#     def removeElement(self, nums, val):
#         k = 0
#         # Iterate through each element in nums
#         for i in range(len(nums)):
#             # If the element is not equal to val, 
#             if nums[i] != val:
#                 nums[k] = nums[i] #store it at index `k`
#                 k += 1  # Increment `k` for the next non-val element

#         # `k` is now the length of the array without `val`
#         return k
