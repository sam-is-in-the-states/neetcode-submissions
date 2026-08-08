class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[-1]*n for _ in range(m)]

        dp[m-1][n-1] = grid[m-1][n-1]

        def helper(i, j):
            if i == m or j == n:
                return float('inf')
            
            if dp[i][j] >= 0:
                return dp[i][j]
            
            ans = grid[i][j] + min(helper(i+1,j), helper(i,j+1))
            dp[i][j] = ans
            return ans
        
        return helper(0,0)