def partitionString(s):
    seen = set()
    partitions = 1
    
    for char in s:
        if char in seen:
            partitions += 1
            seen.clear()
        seen.add(char)
    
    return partitions

# Example Usage
print(partitionString("abac"))  # Output: 2
print(partitionString("world"))  # Output: 1
print(partitionString("aaa"))    # Output: 3
