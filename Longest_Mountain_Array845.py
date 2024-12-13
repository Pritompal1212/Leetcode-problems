def longestMountain(arr):
    n = len(arr)
    max_length = 0

    for i in range(1, n - 1):
        if arr[i - 1] < arr[i] > arr[i + 1]:  # Check for peak
            left, right = i, i
            while left > 0 and arr[left - 1] < arr[left]:  # Expand left
                left -= 1
            while right < n - 1 and arr[right] > arr[right + 1]:  # Expand right
                right += 1
            max_length = max(max_length, right - left + 1)

    return max_length

# Example Usage
arr = [2, 1, 4, 7, 3, 2, 5]
print(longestMountain(arr))  # Output: 5
