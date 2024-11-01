def longestCommonPrefix(strs):
    
    
    
    cp=""
    for i in range(len(strs[0])):
        for j in strs:
            if i==len(j) or j[i] != strs[0][i]:
                return cp
        cp+=strs[0][i]
    return cp
    
strs =["dog","racecar","car"]

print(longestCommonPrefix(strs))
    