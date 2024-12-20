def uniqueOccurrences(arr):
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    
    occurrences = list(count.values())
    return len(occurrences) == len(set(occurrences))

# Example Usage
print(uniqueOccurrences([1, 2, 2, 1, 1, 3]))  # Output: True
print(uniqueOccurrences([1, 2]))             # Output: False
print(uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))  # Output: True
