
def nextGreatestLetter(letters, target):
    left, right = 0, len(letters) - 1

    while left <= right:
        mid = (left + right) // 2
        if letters[mid] > target:
            right = mid - 1  # Move left to find the smallest greater element
        else:
            left = mid + 1  # Move right to find a greater element

    return letters[left] if left < len(letters) else letters[0]

letters = ["c","f","j"]
target = "a"
print(nextGreatestLetter(letters, target))
