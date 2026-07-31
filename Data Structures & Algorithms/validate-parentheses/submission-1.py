class Solution:
    def isValid(self, s: str) -> bool:
        opn = ['(', '{', '[']
        close = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for c in s:
            if c in opn:
                stack.append(c)
                continue
            if not stack or stack[-1] != close[c]:
                return False
            stack.pop()
        return stack == []