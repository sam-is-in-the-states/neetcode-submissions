class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        dp = [[0]*(n+2) for _ in range(n+2)]

        for i in range(2, n+2):
            for j in range(i, n+2):
                if i == j:
                    dp[i][j] = dp[i-1][j]
                    continue
                
                prev_max = max(dp[i-1][j], dp[i][j-1])
                if prices[i-2] >= prices[j-2]:
                    dp[i][j] = prev_max
                    continue
                
                dp[i][j] = max(prev_max, prices[j-2] - prices[i-2] + dp[i-2][i-2])

                

        return dp[n+1][n+1]
