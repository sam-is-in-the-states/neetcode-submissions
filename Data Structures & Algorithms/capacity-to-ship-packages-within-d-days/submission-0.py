class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights) 
        r = len(weights) * l
        ans = r
        while l <= r:
            m = (l+r)//2
            c = 0
            d = 0
            for w in weights:
                if c < w:
                    d += 1
                    c = m
                c -= w

            if d <= days:
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans