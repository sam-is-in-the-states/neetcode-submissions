class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def helper(idx, curr):
            if len(curr) == k:
                ans.append(curr.copy())
                return

            if idx > n:
                return

            for i in range(idx, n + 1):
                curr.append(i)
                helper(i + 1, curr)
                curr.pop()

        helper(1, [])
        return ans