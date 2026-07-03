class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []

        def helper(nums, idx, curr):
            if idx == len(nums):
                ans.append(curr)
                return
            
            helper(nums, idx+1, curr + [nums[idx]])
            next_idx = idx+1
            while next_idx < len(nums) and nums[next_idx] == nums[idx]:
                next_idx += 1
            helper(nums, next_idx, curr)
        
        helper(nums, 0, [])
        return ans
