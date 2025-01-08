def getEncryptedString(s, k):
    n = len(s)
    k = k % n
    result = ""
    for i in range(n):
        result += s[(i + k) % n]
    return result

s = "dart"
k = 3
print(getEncryptedString(s, k))