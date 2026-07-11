class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.helper(nums[:n-1]), self.helper(nums[1:]))
    
    def helper(self, nums: List[int]):
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * n
        dp[n-1] = nums[n-1]
        dp[n-2] = max(nums[n-2], nums[n-1])

        for i in range (n-3, -1, -1):
            dp[i] = max(dp[i+1], nums[i] + dp[i+2])
        
        return dp[0]