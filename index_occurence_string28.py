def find_first_occurrence(haystack, needle):
    if needle in haystack:
            return haystack.find(needle)
    else:
        return -1

haystack ="sadbutsad"
needle = "sad"
result = find_first_occurrence(haystack, needle)
print(result)  


# def find_first_occurrence(haystack, needle):
#     if len(haystack) < len(needle):
#         return -1

#         for i in range(len(haystack)):
#             if haystack[i:i+len(needle)] == needle:
#                 return i

#         return -1 
# haystack="sadbutsad"
# needle = "sad"
# r=find_first_occurrence(haystack, needle)
# print(r)


# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         # Check if needle is longer than haystack
#         if len(haystack) < len(needle):
#             return -1
        
#         # Iterate through haystack to find needle
#         for i in range(len(haystack) - len(needle) + 1):
#             if haystack[i:i+len(needle)] == needle:
#                 return i  # Return the starting index of the first occurrence
        
#         return -1  # If needle is not found

# # Example usage
# if __name__ == '__main__':
#     haystack = input("Enter the haystack string: ")
#     needle = input("Enter the needle string: ")

#     solution = Solution()
#     result = solution.strStr(haystack, needle)
#     print("Index of the first occurrence of needle in haystack:", result)
