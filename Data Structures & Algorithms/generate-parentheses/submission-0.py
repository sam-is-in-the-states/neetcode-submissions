class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(opn, close, curr):
            if opn + close == 0:
                ans.append(curr)
                return
            
            if close > 0:
                helper(opn, close-1, curr + ')')
            
            if opn > 0:
                helper(opn-1, close+1, curr + '(')
        
        helper(n, 0, "")
        return ans

