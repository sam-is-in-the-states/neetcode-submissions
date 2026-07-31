class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 0
        prev = float('-inf')
        
        while j < len(nums):
            if nums[j] > prev:
                prev = nums[j]
                nums[i] = nums[j]
                i += 1
                j += 1
            
            else:
                prev = nums[j]
                j += 1

        return i