def majorityElement(nums):
    n = len(nums)
    b = set(nums)  # Get unique elements
    a = []  # Store elements that occur more than n/3 times

    for x in b:
        count = 0  # Reset count for each unique element
        for num in nums:
            if x == num:
                count += 1
        if count > n / 3:  # Check if the count exceeds n/3
            a.append(x)

    return sorted(a)  # Sort the result to return a consistent order

# Test case
nums = [1, 2]
print(majorityElement(nums))  # Output: [1, 2]
