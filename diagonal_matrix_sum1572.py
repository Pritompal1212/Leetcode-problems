def diagonalSum(mat):
        
    n = len(mat)
        
    mid = n // 2
        
    summation = 0
        
    for i in range(n):
            
            # primary diagonal
        summation += mat[i][i]
            
            # secondary diagonal
        summation += mat[n-1-i][i]
            
            
    if n % 2 == 1:
            # remove center element (repeated) on odd side-length case
        summation -= mat[mid][mid]
            
            
    return summation

mat = [[1,2,3],
        [4,5,6],
        [7,8,9]]
print(diagonalSum(mat))