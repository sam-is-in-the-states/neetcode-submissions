class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = n - 1
            
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                if val == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < n and nums[j] == nums[j-1]:
                        j += 1
                elif val < 0:
                    j += 1
                else:
                    k -= 1   

        return res