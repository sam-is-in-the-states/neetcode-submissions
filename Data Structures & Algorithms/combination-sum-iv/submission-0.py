class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target+1)
        dp[0] = 1

        def helper(t):
            if t < 0:
                return 0
            
            if dp[t] >= 0:
                return dp[t]
            
            ans = 0
            for num in nums:
                ans += helper(t-num)
            
            dp[t] = ans
            return ans
        
        return helper(target)
