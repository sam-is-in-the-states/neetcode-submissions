class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        dp[m-1][n-1] = 1 if obstacleGrid[m-1][n-1] == 0 else 0
        def helper(i, j) -> int:
            if i == m or j == n:
                return 0
            
            if obstacleGrid[i][j] == 1:
                return 0

            if dp[i][j]:
                return dp[i][j]
            
            dp[i][j] = helper(i+1,j) + helper(i,j+1)
            return dp[i][j]
        
        helper(0,0)
        return dp[0][0]