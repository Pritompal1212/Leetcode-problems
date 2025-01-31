
def minScore(nums, k):
    nums.sort()  # Step 1: Sort the array
    n = len(nums)
    min_val = nums[0] + k
    max_val = nums[n-1] - k
    min_score = nums[n-1] - nums[0]  # Initial score without modification

        # Step 2: Try adjusting each element in between
    for i in range(n - 1):
        new_max = max(max_val, nums[i] + k)
        new_min = min(min_val, nums[i + 1] - k)
        min_score = min(min_score, new_max - new_min)

    return min_score
nums = [4, 4, 4]
k = 5
print(minScore(nums, k))
