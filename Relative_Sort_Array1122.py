def relativeSortArray(arr1, arr2):
    # Create a dictionary for the order of elements in arr2
    order = {num: i for i, num in enumerate(arr2)}
    
    # Sort arr1 based on the order in arr2; for elements not in arr2, sort them at the end
    return sorted(arr1, key=lambda x: (order.get(x, len(arr2)), x))

# Example usage
arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
print(relativeSortArray(arr1, arr2))
# Output: [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
