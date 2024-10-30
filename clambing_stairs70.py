
def climbStairs( n):
    if n == 0 or n == 1:
        return 1

        # Initializing the first two steps
    prev, curr = 1, 1

        # Calculate number of ways from step 2 to n
    for i in range(2, n + 1):
        temp = curr
        curr = prev + curr  # Current step value
        prev = temp  # Move prev to the last step

    return curr
n=int(input())
r=climbStairs(n)
print(r)