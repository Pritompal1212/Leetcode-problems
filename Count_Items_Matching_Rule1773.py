def countMatches(items: list, ruleKey: str, ruleValue: str) -> int:
    key_index = {"type": 0, "color": 1, "name": 2}[ruleKey]
    return sum(1 for item in items if item[key_index] == ruleValue)

# Example usage
print(countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver"))  
# Output: 1
