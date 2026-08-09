class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min = None
        curr_max = None
        ans = nums[0]

        for num in nums:
            if curr_max is None:
                curr_max = 1
                curr_min = 1

            curr_max *= num
            curr_min *= num

            if curr_min > curr_max:
                curr_max, curr_min = curr_min, curr_max
            curr_max = max(curr_max, num)
            curr_min = min(curr_min, num)
            ans = max(ans, curr_max)    
        return ans    
