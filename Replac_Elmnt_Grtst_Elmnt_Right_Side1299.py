def replaceElements(arr):
    n = len(arr)
    max_right = -1  # The last element is always replaced with -1

    # Traverse the array from right to left
    for i in range(n - 1, -1, -1):
        new_val = max_right  # Store the max value found so far
        max_right = max(max_right, arr[i])  # Update max_right
        arr[i] = new_val  # Replace the current element
    
    return arr

# Example Usage
print(replaceElements([17, 18, 5, 4, 6, 1]))  # Output: [18, 6, 6, 6, 1, -1]
print(replaceElements([400]))  # Output: [-1]
