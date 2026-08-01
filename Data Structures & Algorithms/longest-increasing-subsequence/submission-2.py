class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [(0,0)]*n

        dp[0] = (nums[0], 1)
        ans = 1

        for i in range(1, n):
            curr = 1
            for j in range(i):
                if dp[j][0] >= nums[i]:
                    continue
                if dp[j][1] >= curr:
                    curr = dp[j][1] + 1
            dp[i] = (nums[i], curr)
            ans = max(ans, curr)
        return ans
