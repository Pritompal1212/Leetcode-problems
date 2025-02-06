def minimumAbsDifference(arr):
    arr.sort()  # Step 1: Sort the array
    min_diff = float('inf')
    result = []
    
    # Step 2: Find the minimum absolute difference
    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        min_diff = min(min_diff, diff)
    
    # Step 3: Collect all pairs with min_diff
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] == min_diff:
            result.append([arr[i], arr[i + 1]])
    
    return result

print(minimumAbsDifference([4, 2, 1, 3]))  
# Output: [[1, 2], [2, 3], [3, 4]]

print(minimumAbsDifference([1, 3, 6, 10, 15]))  
# Output: [[1, 3]]

print(minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]))  
# Output: [[-14, -10], [19, 23], [23, 27]]
