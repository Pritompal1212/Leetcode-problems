def mergeAlternately(word1, word2):
    merged = []
    i, j = 0, 0
    len1, len2 = len(word1), len(word2)

    # Merge alternating characters
    while i < len1 and j < len2:
        merged.append(word1[i])
        merged.append(word2[j])
        i += 1
        j += 1

    # Append remaining characters
    merged.append(word1[i:])
    merged.append(word2[j:])

    return "".join(merged)

# Example Usage
print(mergeAlternately("abc", "pqr"))   # Output: "apbqcr"
print(mergeAlternately("ab", "pqrs"))   # Output: "apbqrs"
print(mergeAlternately("abcd", "pq"))   # Output: "apbqcd"
