# not run

# def plus_one(digits):
#     a=digits[-1]
#     a+=1
#     b=digits.append(a)
#     return b
    
# print(plus_one(1,2,3))


# next one
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
print(plus_one([1, 2, 3]))  # Output should be [1, 2, 4]
print(plus_one([9, 9, 9]))  # Output should be [1, 0, 0, 0]




# def plus_one(digits):
#     i=0
#     while i!=digits[-1]:
#         if digits[i]<9:
#             digits[i]+=1
#         digit[1]=0
#         return digits    
# print(plus_one(1,2,3))