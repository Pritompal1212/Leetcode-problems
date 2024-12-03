def repeatedSubstringPattern(s):
    # Double the string and remove the first and last characters
    doubled_string = (s + s)[1:-1]
    # Check if the original string is present in the modified string
    return s in doubled_string

# Test cases
print(repeatedSubstringPattern("abab"))  # Output: True (constructed by "ab")
print(repeatedSubstringPattern("aba"))   # Output: False
print(repeatedSubstringPattern("abcabcabcabc"))  # Output: True (constructed by "abc")
print(repeatedSubstringPattern("a"))     # Output: False







# def repeatedSubstringPattern(s):
#     n = len(s)
#     for i in range(1, n // 2 + 1):
#         # Check if the current length divides the string completely
#         if n % i == 0:
#             # Extract the substring
#             substring = s[:i]
#             # Repeat the substring and compare with the original string
#             if substring * (n // i) == s:
#                 return True
#     return False

# # Test cases
# print(repeatedSubstringPattern("abab"))  # Output: True (constructed by "ab")
# print(repeatedSubstringPattern("aba"))   # Output: False
# print(repeatedSubstringPattern("abcabcabcabc"))  # Output: True (constructed by "abc")
# print(repeatedSubstringPattern("a"))     # Output: False
