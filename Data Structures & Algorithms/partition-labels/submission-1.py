class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = {}
        for i, char in enumerate(s):
            m[char] = i
        
        ans = []
        size = 0
        max_idx = 0
        for i, char in enumerate(s):
            max_idx = max(max_idx, m[char])
            if i == max_idx:
                ans.append(size+1)
                size = 0
            else:
                size += 1
        
        return ans
