# def duplicateZeros(arr):
#     i = 0
#     j = len(arr)-1
#     while(i < j):
#         if(arr[i] == 0):
#             arr.insert(i+1,0)
#             arr.pop()
#             i += 1
#         i += 1
        
# arr = [1,0,2,3,0,4,5,0]
# print(duplicateZeros(arr))

def duplicateZeros(arr):
    i = 0
    while i < len(arr) - 1:  # Iterate through the array
        if arr[i] == 0:  # If a zero is found
            arr.insert(i + 1, 0)  # Insert an extra zero at the next position
            arr.pop()  # Remove the last element to keep the array length unchanged
            i += 1  # Skip the inserted zero
        i += 1  # Move to the next element

# Example Usage
arr = [1, 0, 2, 3, 0, 4, 5, 0]
duplicateZeros(arr)
print("Modified array:", arr)  # Output: [1, 0, 0, 2, 3, 0, 0, 4]
