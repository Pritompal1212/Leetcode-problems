def isPerfectNumber(num):
    # A perfect number must be greater than 1
    if num <= 1:
        return False

    # Sum of divisors excluding num itself
    sum_of_divisors = 1  # Start with 1, as 1 is a divisor of every number
    sqrt_num = int(num**0.5)  # Square root of num to find divisors efficiently

    # Iterate from 2 to √num to find divisors
    for i in range(2, sqrt_num + 1):
        if num % i == 0:  # If i is a divisor
            sum_of_divisors += i
            if i != num // i:  # Avoid adding the square root twice (e.g., 4 in 16)
                sum_of_divisors += num // i

    # Check if the sum of divisors equals num
    return sum_of_divisors == num

# Input from user
num = int(input("Enter a number: "))
if isPerfectNumber(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
