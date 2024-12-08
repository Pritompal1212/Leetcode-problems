def rotateString(s, goal):
    return len(s) == len(goal) and goal in s + s

s = "abcde"
goal = "cdeab"
print(rotateString(s, goal))