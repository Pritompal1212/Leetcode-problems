def islandPerimeter(grid):
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Found land
                perimeter += 4  # Each land starts with 4 sides
                
                # Check for adjacent land and reduce perimeter accordingly
                if i > 0 and grid[i-1][j] == 1:  # Check top
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:  # Check left
                    perimeter -= 2

    return perimeter

# **Example Usage**
grid1 = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
print(islandPerimeter(grid1))  # Output: 16

grid2 = [
    [1]
]
print(islandPerimeter(grid2))  # Output: 4

grid3 = [
    [1, 1],
    [1, 1]
]
print(islandPerimeter(grid3))  # Output: 8
