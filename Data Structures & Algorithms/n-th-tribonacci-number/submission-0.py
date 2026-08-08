class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n <= 2:
            return 1

        dp = [-1] * (n+1)
        dp[0] = 0
        dp[1] = dp[2] = 1

        def helper(num):
            if dp[num] >= 0:
                return dp[num]
            
            ans = helper(num-1) + helper(num-2) + helper(num-3)
            dp[num] = ans
            return ans
        
        return helper(n)