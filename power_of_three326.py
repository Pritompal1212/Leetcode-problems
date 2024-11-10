def isPowerOfThree(n):
    for x in range(11):
        if 3**x == n:
            return True
        
    return False

print(isPowerOfThree(27))
