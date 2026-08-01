class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, n-2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k, l = j + 1, n - 1
                t = nums[i] + nums[j]
                while k < l:
                    if k > j + 1 and nums[k] == nums[k-1]:
                        k += 1
                        continue
                    if l < n - 1 and nums[l] == nums[l + 1]:
                        l -= 1
                        continue
                    if t + nums[l] + nums[k] == target:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k += 1
                    elif t + nums[l] + nums[k] < target:
                        k += 1
                    else:
                        l -= 1

        return ans