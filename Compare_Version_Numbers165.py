def compareVersion(version1, version2):
    # Split the version strings into their components
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))
    
    # Get the maximum length of the two version lists
    max_len = max(len(v1), len(v2))
    
    # Compare each revision
    for i in range(max_len):
        # Get the i-th revision for both versions, default to 0 if index is out of range
        rev1 = v1[i] if i < len(v1) else 0
        rev2 = v2[i] if i < len(v2) else 0
        
        # Compare the revisions
        if rev1 < rev2:
            return -1
        elif rev1 > rev2:
            return 1
    
    # If all revisions are equal
    return 0

# Test cases
print(compareVersion("1.01", "1.001"))  # Output: 0 (treats leading zeros the same)
print(compareVersion("1.0", "1.0.0"))   # Output: 0 (treats missing revisions as 0)
print(compareVersion("0.1", "1.1"))     # Output: -1 (version1 < version2)
print(compareVersion("1.0.1", "1"))     # Output: 1 (version1 > version2)
