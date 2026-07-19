class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        m = {}
        n = len(nums)
        def helper(idx, curr) -> int:
            if idx == n:
                if curr == target:
                    return 1
                return 0

            if (curr, idx) in m:
                return m[(curr, idx)]
            
            ans = 0
            ans += helper(idx+1, curr+nums[idx])
            ans += helper(idx+1, curr-nums[idx])

            m[(curr, idx)] = ans
            return ans
        
        return helper(0,0)

