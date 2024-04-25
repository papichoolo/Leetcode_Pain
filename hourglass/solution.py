class Solution:
    def findMaxSum(self, n, m, mat):
        if n < 3 or m < 3:
            return -1
        
        max_sum = float('-inf')
        
        for i in range(n - 2):
            for j in range(m - 2):
                # Check if hourglass can be formed
                if i + 2 < n and j + 2 < m:
                    hourglass_sum = mat[i][j] + mat[i][j+1] + mat[i][j+2] + \
                                    mat[i+1][j+1] + \
                                    mat[i+2][j] + mat[i+2][j+1] + mat[i+2][j+2]
                    max_sum = max(max_sum, hourglass_sum)
        
        if max_sum == float('-inf'):
            return -1
        else:
            return max_sum

# Example usage:
sol = Solution()
print(sol.findMaxSum(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Output: 35
print(sol.findMaxSum(2, 3, [[1, 2, 3], [4, 5, 6]]))           # Output: -1