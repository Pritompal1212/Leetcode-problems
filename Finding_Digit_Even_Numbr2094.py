def findEvenNumbers(digits):
    unique_numbers = set()
    n = len(digits)
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if digits[i] != 0 and num % 2 == 0:
                        unique_numbers.add(num)

    return sorted(unique_numbers)

# Example Test Cases
print(findEvenNumbers([1, 2, 3]))
print(findEvenNumbers([2, 2, 8, 8, 2]))
print(findEvenNumbers([3, 7, 5]))
