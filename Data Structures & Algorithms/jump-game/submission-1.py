class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        curr = 0

        for idx, num in enumerate(nums):
            if curr < 0:
                return False

            curr = max(curr, num)
            curr -= 1
        
        return True
