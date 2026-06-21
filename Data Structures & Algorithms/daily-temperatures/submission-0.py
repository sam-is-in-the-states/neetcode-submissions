class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]
        stack = []
        stack.append((temperatures[-1], len(temperatures)-1))
        for i in range(len(temperatures)-2, -1, -1):
            temp = temperatures[i]
            while stack and stack[-1][0] <= temp:
                stack.pop()
            if not stack:
                ans.append(0)
            else:
                ans.append(stack[-1][1] - i)
            stack.append((temp,i))
        return ans[::-1]