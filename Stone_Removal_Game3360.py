# def canAliceWin(n):
#     moves = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#     for i, move in enumerate(moves):
#         if n - move < 0:
#             return i % 2 == 1  # Alice wins on odd indices, Bob on even indices
#         n -= move
#     return True

# # Example Usage
# print(canAliceWin(30))  # Replace 30 with the value you want to test


def canAliceWin(n):
    if n - 10 < 0:
        return False
    n -= 10
    if n - 9 < 0:
        return True
    n -= 9
    if n - 8 < 0:
        return False
    n -= 8
    if n - 7 < 0:
        return True
    n -= 7
    if n - 6 < 0:
        return False
    n -= 6
    if n - 5 < 0:
        return True
    n -= 5
    if n - 4 < 0:
        return False
    n -= 4
    if n - 3 < 0:
        return True
    n -= 3
    if n - 2 < 0:
        return False
    n -= 2
    if n - 1 < 0:
        return True
    n -= 1
    return True

# Example Usage
print(canAliceWin(30))  # Replace 30 with the value you want to test
