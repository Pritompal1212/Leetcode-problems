class Solution:
    def minimumRightShifts(self, nums):
        n = len(nums)
        if nums == sorted(nums):  
            return 0  # Already sorted, no shifts needed
        
        for shift in range(1, n):  
            if nums[shift:] + nums[:shift] == sorted(nums):
                return n - shift  
        
        return -1  # Not possible to sort with right shifts

# Example usage
sol = Solution()
print(sol.minimumRightShifts([1, 3, 5]))  # Output: 0
print(sol.minimumRightShifts([3, 4, 5, 1, 2]))  # Output: 2
print(sol.minimumRightShifts([2, 1, 3, 4]))  # Output: -1
