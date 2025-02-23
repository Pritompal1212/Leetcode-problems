def truncateSentence(s, k):
    return " ".join(s.split()[:k])

# Example Usage
s = "Hello how are you Contestant"
k = 4
print(truncateSentence(s, k))  # Output: "Hello how are you"
