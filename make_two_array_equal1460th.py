def canBeEqual(target, arr):
    return sorted(target) == sorted(arr)

# **Example Usage**
target = [1, 2, 3, 4]
arr = [2, 4, 1, 3]
print(canBeEqual(target, arr))  # Output: True

target = [7, 1, 9]
arr = [7, 9, 1]
print(canBeEqual(target, arr))  # Output: True

target = [1, 2, 3]
arr = [1, 1, 3]
print(canBeEqual(target, arr))  # Output: False
