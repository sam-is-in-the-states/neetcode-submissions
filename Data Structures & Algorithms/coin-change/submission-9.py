class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        import sys
        sys.setrecursionlimit(20000)
        def helper(amount):
            if amount < 0:
                return float('inf')
            
            if amount == 0:
                return 0

            if amount in dp:
                return dp[amount]

            ans = float('inf')
            for c in coins:
                ans = min(ans, 1 + helper(amount - c))
            
            dp[amount] = ans
            return ans
        
        val = helper(amount)
        return val if val != float('inf') else -1