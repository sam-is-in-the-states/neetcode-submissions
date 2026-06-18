class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = nums[0]
        n = len(nums) - 1

        for i, num in enumerate(nums):
            if i > max_idx:
                return False
            max_idx = max(max_idx, i+num)
            if max_idx >= n:
                return True
            
        return False