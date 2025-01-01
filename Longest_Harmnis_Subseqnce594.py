from collections import Counter

def findLHS(nums):
    freq = Counter(nums)
    res = 0
    for num in freq:
        if num + 1 in freq:
            res = max(res, freq[num] + freq[num + 1])
    return res

# Example Usage
nums = [1,3,2,2,5,2,3,7]
print(findLHS(nums))  # Output: 5
