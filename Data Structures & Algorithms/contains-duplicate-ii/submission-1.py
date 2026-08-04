class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        n = len(nums)
        for i in range(min(n, k+1)):
            if nums[i] in m:
                return True
            
            m[nums[i]] = 1

        l = 0
        r = k+1

        while r < n:
            m.pop(nums[l])
            l += 1

            if nums[r] in m:
                return True
            m[nums[r]] = 1
            r += 1
        return False
        
