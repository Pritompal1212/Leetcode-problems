class Solution:
    def buddyStrings(self, s, goal):
        # If lengths are different, they cannot be buddy strings
        if len(s) != len(goal):
            return False

        # If strings are the same, check if there are duplicate characters to swap
        if s == goal:
            return len(set(s)) < len(s)

        # Find the mismatched indices
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)

        # Check if there are exactly two mismatches and swapping makes the strings equal
        return len(diff) == 2 and s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]


# Example Usage
s = "aaaaaaabc"
goal = "aaaaaaacb"
obj = Solution()
print(obj.buddyStrings(s, goal))  # Output: True
