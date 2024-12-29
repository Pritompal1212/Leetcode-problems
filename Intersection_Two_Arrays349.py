class Solution:
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        ans = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:  # nums1[i] == nums2[j]
                ans.append(nums1[i])
                i += 1
                j += 1

        # Remove duplicates
        return list(set(ans))

# Example Usage
solution = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(solution.intersection(nums1, nums2))  # Output: [2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(solution.intersection(nums1, nums2))  # Output: [4, 9]
