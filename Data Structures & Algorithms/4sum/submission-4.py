class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-1):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                k = j + 1
                l = n - 1

                while k < l:
                    val = nums[i] + nums[j] + nums[k] + nums[l]
                    if val == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        while k < n and nums[k] == nums[k-1]:
                            k += 1
                    
                    elif val < target:
                        k += 1
                    
                    else:
                        l -= 1
        return ans