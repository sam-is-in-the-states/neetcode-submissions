class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        fwd = [0] * n
        bwd = [0] * n

        fwd[0] = nums[0]
        bwd[n-1] = nums[n-1]

        for i in range(1, n):
            fwd[i] = fwd[i-1] * nums[i]
            bwd[n-i-1] = bwd[n-i] * nums[n-i-1]

        ans = [0] * n
    
        for i in range(n):
            ans[i] = (fwd[i-1] if i>0 else 1) * (bwd[i+1] if i < n-1 else 1)
        
        return ans

