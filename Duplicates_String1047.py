def removeDuplicates(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Remove the last character from the stack if it's the same as the current one
        else:
            stack.append(char)  # Add the character to the stack if no match is found
    
    return ''.join(stack)  # Reconstruct the string from the stack

# Example usage:
s = "abbaca"
print(removeDuplicates(s))  # Output: "ca"
