class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []

        def helper(n, curr, to_close):
            if n == 0 and to_close == 0:
                ans.append(curr)
                return
            
            if to_close > 0:
                helper(n, curr + ')', to_close-1)
            
            if n > 0:
                helper(n-1, curr + '(', to_close+1)
        helper(n, "", 0)
        return ans
