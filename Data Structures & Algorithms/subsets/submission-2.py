class Solution:
    ans = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.subsets2(nums, 0, [])
        return self.ans
    
    def subsets2(self, nums, idx, l):
        if idx == len(nums):
            self.ans.append(list(l))
            return
        self.subsets2(nums, idx+1, l)
        self.subsets2(nums, idx+1, l+[nums[idx]])
        

