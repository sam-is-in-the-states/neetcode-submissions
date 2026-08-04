class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        n = len(nums)
        ans = n
        
        i,j = 0, 0
        curr = 0
        while j < n:
            curr += nums[j]

            while curr >= target:
                ans = min(ans, j-i+1)
                curr -= nums[i]
                i += 1
            j += 1
            
        return ans