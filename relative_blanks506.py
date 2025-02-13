def findRelativeRanks(score):
    sorted_scores = sorted(score, reverse=True)  # Sort in descending order
    rank_map = {}

    # Assign ranks
    for i, val in enumerate(sorted_scores):
        if i == 0:
            rank_map[val] = "Gold Medal"
        elif i == 1:
            rank_map[val] = "Silver Medal"
        elif i == 2:
            rank_map[val] = "Bronze Medal"
        else:
            rank_map[val] = str(i + 1)  # Convert placement to string
    
    # Create result based on original order
    return [rank_map[s] for s in score]

# **Example Usage**
score = [10, 3, 8, 9, 4]
print(findRelativeRanks(score))  
# Output: ['Gold Medal', '5', 'Bronze Medal', 'Silver Medal', '4']
