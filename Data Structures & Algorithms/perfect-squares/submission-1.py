class Solution:
    def numSquares(self, n: int) -> int:
        dp = [-1] * (n+1)
        dp[0] = 0
        def helper(num):
            if dp[num] >= 0:
                return dp[num]

            val = int(math.sqrt(num))

            ans = num

            for i in range(val,1,-1):
                ans = min(ans, 1 + helper(num - i*i))
            
            dp[num] = ans
            return ans
        return helper(n)
