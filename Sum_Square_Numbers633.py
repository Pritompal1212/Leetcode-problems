import math
def judgeSquareSum(c):
    left, right = 0, int(math.sqrt(c))

    while left <= right:
        total = left * left + right * right
        if total == c:
            return True
        elif total < c:
            left += 1
        else:
            right -= 1

    return False

c=5
print(judgeSquareSum(c))
