class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [-1] * (n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 1

        def helper(num):
            if dp[num] >= 0:
                return dp[num]
            
            ans = 0

            for i in range(1, num):
                ans = max(ans, i * (num - i), i * helper(num - i))
            
            dp[num] = ans
            return ans
        
        return helper(n)