class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i,j,k = -1,0,n

        while j < k:
            if nums[j] == 0:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
            elif nums[j] == 2:
                k -= 1
                nums[j], nums[k] = nums[k], nums[j]
            else:
                j += 1
        
