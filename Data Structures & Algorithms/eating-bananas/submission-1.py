class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = h

        l = 1
        r = max(piles)

        while l <= r:
            m = (l + r) // 2
            temp = 0
            
            for p in piles:
                temp += math.ceil(p / m)
            
            if temp <= h:
                ans = m
                r = m - 1
            
            else:
                l = m + 1
        
        return ans