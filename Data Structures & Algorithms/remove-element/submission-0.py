class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = -1

        while i < len(nums):
            if nums[i] != val:
                j += 1
                nums[j], nums[i] = nums[i], nums[j]
            i += 1
        return j+1