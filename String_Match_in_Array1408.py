def stringMatching(words):
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and words[i] in words[j]:
                result.append(words[i])
                break  # Avoid duplicate entries
    return result

words = ["mass", "as", "hero", "superhero"]
print(stringMatching(words))  # Output: ["as", "hero"]
