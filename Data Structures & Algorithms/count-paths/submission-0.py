class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None]*n for _ in range(m)]
        dp[m-1][n-1] = 1
        def helper(i, j) -> int:
            if i == m or j == n:
                return 0
            
            if dp[i][j]:
                return dp[i][j]
            
            dp[i][j] = helper(i+1,j) + helper(i,j+1)
            return dp[i][j]
        
        helper(0,0)
        return dp[0][0]
