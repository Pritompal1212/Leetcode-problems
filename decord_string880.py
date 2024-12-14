def decodeAtIndex(s, k):
    size = 0

    # Calculate the size of the decoded string
    for char in s:
        size = size * int(char) if char.isdigit() else size + 1

    # Work backward to find the k-th character
    for char in reversed(s):
        k %= size
        if k == 0 and char.isalpha():
            return char
        size = size // int(char) if char.isdigit() else size - 1

# Example Usage
s = "leet2code3"
k = 10
print(decodeAtIndex(s, k))  # Output: "o"
