def removeDigits(s: str) -> str:
    stack = []
    
    for char in s:
        if char.isdigit():
            while stack and not stack[-1].isdigit():
                stack.pop()
                break
        else:
            stack.append(char)
    
    return "".join(stack)

# Example usage
print(removeDigits("a1b2c3"))  # Output: ""
print(removeDigits("abc123"))  # Output: ""
print(removeDigits("a1bc2d3")) # Output: "d"
