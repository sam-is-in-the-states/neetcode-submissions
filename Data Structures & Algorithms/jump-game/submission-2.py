class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = 0

        for i in range(len(nums)):
            if i > n:
                return False
            
            n = max(n, i+nums[i])
        
        return True