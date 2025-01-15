def removeKdigits(num, k):
    # Stack to maintain the digits
    stack = []

    # Iterate through each digit in the number
    for digit in num:
        # Remove digits from the stack if they are greater than the current digit
        # and we still need to remove more digits
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # Remove remaining digits from the end if k > 0
    while k > 0:
        stack.pop()
        k -= 1

    # Convert the stack back to a number string and remove leading zeros
    result = ''.join(stack).lstrip('0')

    # If the result is empty, return "0"
    return result if result else "0"
# Example 1
num = "1432219"
k = 3
print(removeKdigits(num, k))  # Output: "1219"

# Example 2
num = "10200"
k = 1
print(removeKdigits(num, k))  # Output: "200"

# Example 3
num = "10"
k = 2
print(removeKdigits(num, k))  # Output: "0"
