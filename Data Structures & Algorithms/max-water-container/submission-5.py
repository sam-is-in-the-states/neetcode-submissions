class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        ans = -1

        while l < r:
            curr = min(heights[l], heights[r]) * (r - l)
            ans = max(curr, ans)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return ans