class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = max(piles)

        l = 1
        r = ans

        while l <= r:
            m = (l + r) // 2
            time = 0
            for b in piles:
                time += math.ceil(b/m)
            
            if time <= h:
                ans = m
                r = m - 1
            
            else:
                l = m + 1
        
        return ans