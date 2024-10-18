class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:  # If the list is empty, return 0
            return 0
        
        j = 0  # Pointer for the current unique position
        
        for i in range(1, len(nums)):  # Start from index 1
            if nums[i] != nums[j]:  # If we find a new unique element
                j += 1  # Move the pointer for unique position
                nums[j] = nums[i]  # Set the next unique element
        
        return j + 1  # Return the number of unique elements

# Example of usage:
sol = Solution()
nums = [0,0,1, 1,1, 2, 2, 3,3, 4]  # Sample sorted array with duplicates
length = sol.removeDuplicates(nums)  # Call the method to remove duplicates

# Print the results:
print("Number of unique elements:", length)  # Output: 4
print("Modified array with unique elements:", nums[:length])  # Output: [1, 2, 3, 4]

    
    
  
