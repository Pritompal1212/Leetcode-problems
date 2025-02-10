def reverseVowels(s: str) -> str:
    vowels = set("aeiouAEIOU")  # Set of vowels
    s = list(s)  # Convert string to a list (to allow modifications)
    
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]  # Swap vowels
            left += 1
            right -= 1
        if s[left] not in vowels:
            left += 1
        if s[right] not in vowels:
            right -= 1

    return "".join(s)  # Convert list back to string

# **Example Usage**
print(reverseVowels("hello"))      # Output: "holle"
print(reverseVowels("leetcode"))   # Output: "leotcede"
print(reverseVowels("AEIOU"))      # Output: "UOIEA"
print(reverseVowels("abcde"))      # Output: "ebcda"
