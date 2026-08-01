class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        ans = -1
        while l < r:
            lh = heights[l]
            rh = heights[r]
            ans = max(ans, min(lh,rh)*(r-l))

            if lh < rh:
                l += 1
            else:
                r -= 1

        return ans  

