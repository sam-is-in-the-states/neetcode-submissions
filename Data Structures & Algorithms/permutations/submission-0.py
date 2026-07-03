class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(nums, curr):
            if not nums:
                ans.append(curr.copy())
            vals = list(nums)
            for item in vals:
                nums.remove(item)
                curr.append(item)
                helper(nums, curr)
                curr.pop()
                nums.add(item)
            
        helper(set(nums), [])
        return ans