# nums1=[1,2,3,0,0,0,]
# m=len(nums1)
# nums2=[2,5,6]
# n=len(nums2)

# arr=[]
# arr=nums1+nums2

# print(arr)



# def merge_sorted_arr(nums1,nums2):
#     # # return arr
#     # for i in range(len(arr)):
#     #     if i==0:
#     #         return arr.remove()
#     arr=[x for x in nums1 if x != 0 ] + nums2
#     return arr.sort()


# nums1=[1,2,3,0,0,0]
# nums2=[2,5,6]

# r=merge_sorted_arr(nums1,nums2)
# print(r)



def merge_sorted_arr(nums1, nums2):
    # Filter out the zero placeholders in nums1 and combine both lists
    arr = [x for x in nums1 if x != 0] + nums2
    
    # Sort the combined list
    arr.sort()
    
    return arr

# Test the function
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
print(merge_sorted_arr(nums1, nums2))  # Expected output: [1, 2, 2, 3, 5, 6]
