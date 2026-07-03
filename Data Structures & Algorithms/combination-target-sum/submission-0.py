class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def helper(nums, idx, target, curr):
            if target == 0:
                ans.append(curr)
                return
            
            if target < 0:
                return
            
            if idx == len(nums):
                return
            
            helper(nums, idx, target - nums[idx], curr + [nums[idx]])
            helper(nums, idx+1, target, curr)
        
        helper(nums, 0, target, [])
        return ans

        