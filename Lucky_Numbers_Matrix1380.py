
def luckyNumbers(matrix):
    min_in_rows = {min(row) for row in matrix}  # Find min of each row
    max_in_cols = {max(col) for col in zip(*matrix)}  # Find max of each column
    return list(min_in_rows & max_in_cols)
matrix = [[3,7,8],[9,11,13],[15,16,17]]
print(luckyNumbers(matrix))
