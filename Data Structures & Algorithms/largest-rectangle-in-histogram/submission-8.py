class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                idx = stack.pop()

                left = stack[-1] if stack else -1
                width = i - left - 1

                ans = max(ans, heights[idx] * width)

            stack.append(i)

        n = len(heights)

        while stack:
            idx = stack.pop()

            left = stack[-1] if stack else -1
            width = n - left - 1

            ans = max(ans, heights[idx] * width)

        return ans