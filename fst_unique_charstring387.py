def firstUniqChar(s):
    # Step 1: Count frequency of each character
    frequency = {}
    for i in range(len(s)):
        char = s[i]
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Step 2: Find the first character with a frequency of 1
    for i in range(len(s)):
        if frequency[s[i]] == 1:
            return i

    # If no unique character is found
    return -1

# Example usage
s = "loveleetcode"
print(firstUniqChar(s))  # Output: 2

s = "aabb"
print(firstUniqChar(s))  # Output: -1
