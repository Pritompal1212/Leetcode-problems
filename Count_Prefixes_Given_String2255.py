class Solution:
    def countPrefixes(self, words, s):
        return sum(1 for word in words if s.startswith(word))

# Example usage
sol = Solution()
print(sol.countPrefixes(["a", "b", "ab", "abc"], "abc"))  # Output: 3
