def findNumbers(nums):
    return sum(1 for num in nums if len(str(num)) % 2 == 0)
nums = [12,345,2,6,7896]
print(findNumbers(nums))