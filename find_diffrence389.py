def findTheDifference(s, t):
    sum_s=sum(ord(char)for char in s)
    sum_t=sum(ord(char)for char in t)
    return chr(sum_t-sum_s)
s = "abcd"
t = "abcde"
print(findTheDifference(s, t))  
