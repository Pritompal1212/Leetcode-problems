def findMiddleIndex(nums):
    total_sum = sum(nums)  # Compute the total sum of the array
    left_sum = 0  # Initialize the left sum
    
    for i in range(len(nums)):
        right_sum = total_sum - left_sum - nums[i]  # Compute right sum
        if left_sum == right_sum:
            return i  # Return the leftmost valid middleIndex
        left_sum += nums[i]  # Update left sum for next iteration

    return -1  # Return -1 if no middleIndex is found

# Example test cases:
print(findMiddleIndex([2,3,-1,8,4]))  # Output: 3
print(findMiddleIndex([1,-1,4]))      # Output: 2
print(findMiddleIndex([2,5]))         # Output: -1
