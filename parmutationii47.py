
def permuteUnique(nums):
    def backtrack(path, used):
        if len(path) == len(nums):  
            result.append(path[:])  # Add a copy of the permutation
            return
            
        for i in range(len(nums)):
                # Skip already used elements
            if used[i]:
                continue
                
                # Skip duplicate elements
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue  
                
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False

    nums.sort()  # Sorting helps in skipping duplicates
    result = []
    backtrack([], [False] * len(nums))
    return result
nums = [1,1,2]
print( permuteUnique(nums))