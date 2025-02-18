def numSpecial(mat):
    m, n = len(mat), len(mat[0])
    
    # Compute row and column sums
    rowSum = [sum(row) for row in mat]
    colSum = [sum(mat[i][j] for i in range(m)) for j in range(n)]

    print("Row Sums:", rowSum)
    print("Column Sums:", colSum)
    
    count = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1 and rowSum[i] == 1 and colSum[j] == 1:
                print(f"Special position found at: ({i}, {j})")
                count += 1
                
    return count

# Test Case
test_matrix = [[1, 0, 0],
               [0, 1, 0],
               [0, 0, 1]]
print("Special positions count:", numSpecial(test_matrix))

