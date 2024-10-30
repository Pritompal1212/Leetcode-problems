def lengthOfLastWord(s):
    word=s.split()
    return len(word[-1])

print(lengthOfLastWord("    fly me    to    the moon  "))
