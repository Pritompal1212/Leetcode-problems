def kthDistinct(arr, k):
    count = {}  

    for s in arr:
        count[s] = count.get(s, 0) + 1

    distinct = [s for s in arr if count[s] == 1]  
    
    return distinct[k-1] if k <= len(distinct) else ""

# Add test cases here
print(kthDistinct(["a", "b", "a", "c", "b", "d"], 2)) 