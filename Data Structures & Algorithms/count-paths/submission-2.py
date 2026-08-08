class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        def helper(i, j):
            if i == m - 1:
                return 1
            
            if j == n - 1:
                return 1

            if dp[i][j] > 0:
                return dp[i][j]

            ways = helper(i+1, j) + helper(i, j+1)
            dp[i][j] = ways

            return ways
        
        return helper(0,0)
