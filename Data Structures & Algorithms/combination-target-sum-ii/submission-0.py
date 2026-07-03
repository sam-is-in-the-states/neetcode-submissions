class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        nums = sorted(candidates)
        def helper(nums, idx, target, curr):
            if target == 0:
                ans.append(curr)
                return
            
            if target < 0:
                return
            
            if idx == len(nums):
                return
            
            helper(nums, idx+1, target - nums[idx], curr + [nums[idx]])
            next_idx = idx+1
            while next_idx < len(nums) and nums[next_idx] == nums[idx]:
                next_idx += 1
            helper(nums, next_idx, target, curr)
        
        helper(nums, 0, target, [])
        return ans