class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st = 0
        end = len(nums) - 1

        while st <= end:
            mid = (st + end)//2
            n = nums[mid]

            if n == target:
                return mid
            
            if n > target:
                end = mid - 1
            else:
                st = mid + 1
        
        return -1