
def twosum(arr,target):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                return [i,j]
    return None
    
arr=[2,7,11,15]
target=9

r=twosum(arr,target)
print(r)
    
    
# class Soln:
#     def twosum(self, arr, target):  # Adding 'self' as first argument
#         for i in range(len(arr)):
#             for j in range(i + 1, len(arr)):
#                 if arr[i] + arr[j] == target:
#                     return [i, j]
#         return None  # Return None or some indication if no solution is found

# arr = [2, 7, 11, 15]
# target = 9

# soln = Soln()
# r = soln.twosum(arr, target)
# print(r)