# def mostCommonWord(paragraph, banned):
#     paragraph = " ".join(re.findall(r"[a-zA-Z0-9]+", paragraph))
#     c = Counter(paragraph.lower().split())
#     c = OrderedDict(c.most_common())
#     for word in c:
#         if word not in banned:
#             return word
        
# paragraph = "a"
# banned = []
# print(mostCommonWord(paragraph, banned))


import re
from collections import Counter, OrderedDict

def mostCommonWord(paragraph, banned):
    # Use regular expression to clean the paragraph
    paragraph = " ".join(re.findall(r"[a-zA-Z0-9]+", paragraph))
    
    # Count the words and sort by frequency
    c = Counter(paragraph.lower().split())
    c = OrderedDict(c.most_common())
    
    # Find the most common word not in banned
    for word in c:
        if word not in banned:
            return word

# Example input
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

# Output the result
print(mostCommonWord(paragraph, banned))
