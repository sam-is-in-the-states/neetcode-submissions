class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 0
        prev = float('-inf')
        
        while j < len(nums):
            if nums[j] > prev:
                nums[i] = nums[j]
                i += 1
            
            prev = nums[j]
            j += 1

        return i