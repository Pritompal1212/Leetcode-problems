def uncommonWords(s1, s2):
    # Split both sentences into words
    words = s1.split() + s2.split()
    
    # Count the frequency of each word
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    # Find words that appear exactly once
    result = [word for word in word_count if word_count[word] == 1]
    
    return result

# Test cases
print(uncommonWords("this is a test", "this is a demo"))  # Output: ['test', 'demo']
print(uncommonWords("apple banana", "banana orange apple"))  # Output: ['orange']
print(uncommonWords("hello world", "world"))  # Output: ['hello']
