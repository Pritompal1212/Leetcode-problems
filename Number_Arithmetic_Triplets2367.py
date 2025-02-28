def arithmeticTriplets(nums, diff):
    count = 0
    num_set = {num for num in nums}
    
    for num in nums:
        if num + diff in num_set and num + 2 * diff in num_set:
            count += 1
    
    return count

# Example Test Cases
print(arithmeticTriplets([0, 1, 4, 6, 7, 10], 3))
print(arithmeticTriplets([4, 5, 6, 7, 8, 9], 2))
