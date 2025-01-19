import heapq

def findKthLargest(nums, k):
    # Create a min-heap of the first k elements
    heap = nums[:k]
    heapq.heapify(heap)

    # For the remaining elements, maintain the heap size at k
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappop(heap)  # Remove the smallest element
            heapq.heappush(heap, num)  # Add the new element

    # The root of the heap (heap[0]) is the k-th largest element
    return heap[0]

# Example usage
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))  # Output: 5
