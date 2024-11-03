def isPowerOfTwo(n):
    for x in range(0,11):
        if 2**x==n:
            return True
        
    return False
n=16
print(isPowerOfTwo(n))