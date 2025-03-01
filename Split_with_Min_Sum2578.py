def splitNum(num):
    digits = sorted(str(num))
    num1, num2 = "", ""

    for i, digit in enumerate(digits):
        if i % 2 == 0:
            num1 += digit
        else:
            num2 += digit

    return int(num1) + int(num2)

# Example Test Cases
print(splitNum(4325))
print(splitNum(687))
