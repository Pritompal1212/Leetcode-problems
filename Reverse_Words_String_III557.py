def reverseWords(s: str) -> str:
    # Step 1: Split the sentence into a list of words
    words = s.split(" ")  # Splits by spaces, keeping multiple spaces as empty strings
    
    # Step 2: Reverse each word in the list
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])  # Reverse the characters in each word
    
    # Step 3: Join the reversed words back into a sentence with spaces
    result = " ".join(reversed_words)
    
    return result

# Examples
input_1 = "Let's take LeetCode contest"
print(reverseWords(input_1))  # Output: "s'teL ekat edoCteeL tsetnoc"

input_2 = "Hello World"
print(reverseWords(input_2))  # Output: "olleH dlroW"

input_3 = "  hello   world  "
print(reverseWords(input_3))  # Output: "  olleh   dlrow  "
