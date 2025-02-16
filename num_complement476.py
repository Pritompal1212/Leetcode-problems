def findComplement(num):
    mask = (1 << num.bit_length()) - 1  # Create a mask of all 1's
    return num ^ mask  # XOR to flip bits

# **Example Usage**
print(findComplement(5))  # Output: 2
print(findComplement(1))  # Output: 0
print(findComplement(10))  # Output: 5
