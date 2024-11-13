def numJewelsInStones(jewels, stones):
    # Initialize a counter for jewels in stones
    jewel_count = 0

    # Iterate over each stone in `stones`
    for stone in stones:
        # If the stone type is in `jewels`, increment the count
        if stone in jewels:
            jewel_count += 1

    return jewel_count

# Example usage:
jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones)) 