def longestWord(words):
    # Sort the words to handle lexicographical order and build incrementally
    words.sort()
    valid_words = set([""])  # Start with an empty word as valid
    longest_word = ""

    for word in words:
        # Check if the prefix (word without last character) is valid
        if word[:-1] in valid_words:
            valid_words.add(word)  # Add the word to valid set
            # Update the longest word if the current word is longer or same length but smaller lexicographically
            if len(word) > len(longest_word):
                longest_word = word

    return longest_word

words = ["w", "wo", "wor", "worl", "world", "a", "ap", "app", "appl", "apple", "apples"]
print(longestWord(words))  # Output: "world"
