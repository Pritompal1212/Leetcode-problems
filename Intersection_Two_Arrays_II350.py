def intersect(nums1, nums2):
    # Create a dictionary to count the occurrences in nums1
    count = {}
    for num in nums1:
        count[num] = count.get(num, 0) + 1
    
    # Find the intersection
    result = []
    for num in nums2:
        if num in count and count[num] > 0:
            result.append(num)
            count[num] -= 1  # Decrease the count in the dictionary
    
    return result

# Example usage:
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersect(nums1, nums2))  # Output: [4, 9]
