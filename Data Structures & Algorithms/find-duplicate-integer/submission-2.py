class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        i = 0

        while i < len(nums):
            if nums[i] - 1 == i:
                i += 1
                continue
            
            num = nums[i]

            if nums[num - 1] == nums[i]:
                return num
            nums[num - 1], nums[i] = nums[i], nums[num - 1]
