'''
def rotate(matrix):
    n=len(matrix)
    for row in range(n // 2):
        for col in range(row, n - row - 1):
                # Swap the top-left and top-right cells in the current group
            matrix[row][col], matrix[col][n - 1 - row] = (
                matrix[col][n - 1 - row],
                matrix[row][col],
            )

                # Swap the top-left and bottom-right cells in the current group
            matrix[row][col], matrix[n - 1 - row][n - 1 - col] = (
                matrix[n - 1 - row][n - 1 - col],
                matrix[row][col],
            )

                # Swap the top-left and bottom-left cells in the current group
            matrix[row][col], matrix[n - 1 - col][row] = (
                matrix[n - 1 - col][row],
                matrix[row][col],
            )
'''
    
        
def rotate(matrix):
    n = len(matrix)        
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Test the function
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
print(matrix)
