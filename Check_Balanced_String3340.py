def isBalanced(num):
    even_sum = 0
    odd_sum = 0
    for i, digit in enumerate(num):
        if i % 2 == 0:  # Even index
            even_sum += int(digit)
        else:  # Odd index
            odd_sum += int(digit)
    return even_sum == odd_sum

# Examples
num1 = "1230"
print(isBalanced(num1))  # Output: True (1+3 = 2+0)

num2 = "12345"
print(isBalanced(num2))  # Output: False (1+3+5 ≠ 2+4)
