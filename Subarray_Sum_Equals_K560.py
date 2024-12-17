def subarraySum(nums, k):
    prefix_sum, count, prefix_count = 0, 0, {0: 1}
    for num in nums:
        prefix_sum += num
        count += prefix_count.get(prefix_sum - k, 0)
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
    return count

# Example Usage
nums = [1, 2, 3]
k = 3
print(subarraySum(nums, k))  # Output: 2
