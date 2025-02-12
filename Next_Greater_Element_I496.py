def nextGreaterElement(nums1, nums2):
    stack = []
    next_greater = {}

    # Process nums2 from right to left
    for num in reversed(nums2):
        # Maintain a decreasing monotonic stack
        while stack and stack[-1] <= num:
            stack.pop()
        
        # If stack is not empty, top is the next greater element
        next_greater[num] = stack[-1] if stack else -1
        stack.append(num)

    # Map results for nums1 from next_greater dictionary
    return [next_greater[num] for num in nums1]

# **Example Usage**
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(nextGreaterElement(nums1, nums2))  # Output: [-1, 3, -1]

nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(nextGreaterElement(nums1, nums2))  # Output: [3, -1]
