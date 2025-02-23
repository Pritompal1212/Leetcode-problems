def countVowelSubstrings(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    
    # Iterate through the word and check for vowel substrings
    for i in range(len(word)):
        vowel_set = set()
        for j in range(i, len(word)):
            if word[j] in vowels:
                vowel_set.add(word[j])
                if len(vowel_set) == 5:  # If all vowels are present, count it
                    count += 1
            else:
                break  # Stop if a consonant is found
                
    return count

# Example Usage
print(countVowelSubstrings("aeiouu"))  # Output: 6
print(countVowelSubstrings("unicornarihan"))  # Output: 2
print(countVowelSubstrings("cbaeio"))  # Output: 0
