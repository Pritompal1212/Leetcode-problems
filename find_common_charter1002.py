def commonChars(words):
    # Step 1: Initialize frequency count with the first word
    common_freq = {}
    for char in words[0]:
        common_freq[char] = common_freq.get(char, 0) + 1

    # Step 2: Iterate through the rest of the words
    for word in words[1:]:
        word_freq = {}
        for char in word:
            word_freq[char] = word_freq.get(char, 0) + 1
        
        # Update common frequency dictionary
        for char in list(common_freq.keys()):
            if char in word_freq:
                common_freq[char] = min(common_freq[char], word_freq[char])
            else:
                del common_freq[char]  # Remove character if not found in current word

    # Step 3: Construct the result list
    result = []
    for char in common_freq:
        result += [char] * common_freq[char]

    return result

words = ["bella","label","roller"]
print(commonChars(words))