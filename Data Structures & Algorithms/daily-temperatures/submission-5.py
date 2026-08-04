class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        ans = [0] * n
        idx = n - 2
        s = [(temperatures[-1], n-1)]
        while idx >= 0:
            while s and s[-1][0] <= temperatures[idx]:
                s.pop()
            
            if not s:
                ans[idx] = 0
            else:
                ans[idx] = s[-1][1] - idx
            s.append((temperatures[idx], idx))
            idx -= 1
        return ans