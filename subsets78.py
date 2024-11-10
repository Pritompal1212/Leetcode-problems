def subsets(nums):
    result = []

    def backtrack(start, path):
        # Add the current subset to the result
        result.append(path[:])
        
        # Explore further subsets
        for i in range(start, len(nums)):
            # Include the current element
            path.append(nums[i])
            # Move to the next element
            backtrack(i + 1, path)
            # Backtrack: remove the last element
            path.pop()

    # Start backtracking from the first index
    backtrack(0, [])
    return result

# Test the function
nums = [1, 2, 3]
print(subsets(nums))
