def sortedSquares(nums):
    arr = []
    for i in nums:
        arr.append(i ** 2)  # Append the square of each number to the list
    arr.sort()  # Sort the list in place
    return arr

# Example Usage
nums = [-4, -1, 0, 3, 10]
nums = [-7,-3,2,3,11]
print(sortedSquares(nums))  # Output: [0, 1, 9, 16, 100]
