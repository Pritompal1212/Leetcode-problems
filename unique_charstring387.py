def firstUniqChar(s):
    st=0
    en=len(s)-1
    while st!=en:
        if st == en:
            return -1
        else:
            return 0

s = "loveleetcode"
print(firstUniqChar(s))