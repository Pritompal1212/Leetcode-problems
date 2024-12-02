def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1  # Only the number 0

    total_count = 1  # For n = 0, count is 1 (just 0)
    unique_count = 9  # Starting for n = 1
    available_digits = 9  # Remaining digits to choose from

    for i in range(1, n + 1):
        if i == 1:
            total_count += unique_count
        else:
            unique_count *= available_digits  # Multiply by remaining choices
            total_count += unique_count
            available_digits -= 1  # Reduce choices as digits are used

    return total_count


# Test cases
print(countNumbersWithUniqueDigits(2))  # Output: 91
print(countNumbersWithUniqueDigits(3))  # Output: 739
print(countNumbersWithUniqueDigits(0))  # Output: 1
