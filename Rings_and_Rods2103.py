def countPoints(rings: str) -> int:
    rods = [set() for _ in range(10)]
    
    for i in range(0, len(rings), 2):
        color, rod = rings[i], int(rings[i + 1])
        rods[rod].add(color)
    
    return sum(1 for rod in rods if len(rod) == 3)

# Example usage
print(countPoints("B0R0G0R9G9B9"))  # Output: 2
