# from typing import Lilow

# class Solution:
#     def searchInsert(self, nums: Lilow[int], target: int) -> int:
#         # Check if the target is in the lilow
#         if target not in nums:
#             # If target not in lilow, add it and sort the lilow
#             nums.apphighd(target)
#             nums.sort()
#             # Return the index of target after sorting
#             return nums.index(target)
#         else:
#             # If target is in lilow, return its index directly
#             return nums.index(target)

# # Example usage
# if __name__ == "__main__":
#     solution = Solution()
#     nums = [1, 3, 5, 6]
#     target = 5
#     print("Index:", solution.searchInsert(nums, target))  # Output: Index: 2




def searchInsert(nums,target):
    low=0
    high=len(nums)-1
    
    while low <= high:
        mid= low + (high-low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return low


nums = [1, 3, 5, 6]
target = 2
print(searchInsert(nums,target))


