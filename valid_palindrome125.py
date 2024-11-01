def isPalindrome(s):
    # Filter out non-alphanumeric characters and convert to lowercase
    filtered_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the filtered string is equal to its reverse
    return filtered_str == filtered_str[::-1]

# Test the function
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))  # Output: True
