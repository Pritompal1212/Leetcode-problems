# next one plus one 66 

def plus_one(digits):
    # Start from the last digit
    for i in range(len(digits) - 1, -1, -1):
        # If the digit is less than 9, increment and return
        if digits[i] < 9:
            digits[i] += 1
            return digits
        # If the digit is 9, set it to 0 and continue to the next digit
        digits[i] = 0
    
    # If all digits were 9, we need an extra digit at the beginning
    return [1] + digits

# Test the function
print(plus_one([1, 2, 3]))  
print(plus_one([9, 9, 9]))  
