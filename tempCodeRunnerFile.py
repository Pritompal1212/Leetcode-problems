def mostCommonWord(paragraph, banned):
#     paragraph = " ".join(re.findall(r"[a-zA-Z0-9]+", paragraph))
#     c = Counter(paragraph.lower().split())
#     c = OrderedDict(c.most_common())
#     for word in c:
#         if word not in banned:
#             return word
        
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# print(mostCommonWord(paragraph, banned))