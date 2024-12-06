def findPeakElement(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        # Check if mid is part of the increasing sequence
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            # Mid is part of the decreasing sequence or the peak
            right = mid
    
    # Left and right will converge to the peak index
    return left

# Example usage:
arr = [1, 3, 5, 7, 6, 4, 2]
print("Peak index:", findPeakElement(arr))  # Output: 3 (index of peak 7)
