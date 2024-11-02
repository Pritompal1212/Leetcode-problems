# HARD 
 
#but its not a ligalmethod
# def merge_sorted_arr(nums1, nums2):
#     if len(nums1) < len(nums2):
#         nums2.extend(nums1)
#         nums2.sort()
#         mid1=(nums2[0]+nums2[-1])/2
#         return mid1
#     else:
#         nums1.extend(nums2)
#         nums1.sort()
#         mid2=(nums1[0]+nums1[-1])/2
#         return mid2
    
# nums1 = [1,2]
# nums2 = [3,4]
# print(merge_sorted_arr(nums1, nums2)) 


#my one
# def findMedianSortedArrays(nums1, nums2):
#         nums = nums1 + nums2
#         nums = sorted(nums)
#         mid=len(nums)//2

#         if len(nums) %2 != 0:
#             return nums[mid]
#         else:
#             mid=(nums[mid-1] + nums[mid])
#             return mid / 2.0
# nums1 = [1,2]
# nums2 = [3,4]
# print(findMedianSortedArrays(nums1, nums2)) 


#best run time

def findMedianSortedArrays(nums1, nums2):
        sum = 0
        merge = nums1 + nums2
        merge.sort()
        n = len(merge)
        if (n % 2 == 0):
            mid1 = merge[n // 2 - 1]
            mid2 = merge[n // 2]
            median = (mid1 + mid2) / 2.0
        else:
            median = merge[n // 2]
        return median
nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1, nums2)) 
