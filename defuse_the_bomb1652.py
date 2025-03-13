class Solution:
    def decrypt(self, code, k):
        n = len(code)
        res = [0] * n

        if k == 0:
            return res
        
        for i in range(n):
            if k > 0:
                res[i] = sum(code[(i + j) % n] for j in range(1, k + 1))
            else:
                res[i] = sum(code[(i + j) % n] for j in range(k, 0))

        return res

# Example usage
sol = Solution()
print(sol.decrypt([5, 7, 1, 4], 3))  # Output: [12, 10, 16, 13]
