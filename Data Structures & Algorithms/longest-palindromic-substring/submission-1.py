class Solution:
    def longestPalindrome(self, s: str) -> str:
        from pprint import pprint
        n = len(s)
        dp = [[None] * n for _ in range(n)]

        ans = s[0]
        l = 1
        
        def helper(i, j):
            if i > j:
                return False
            
            if i == j:
                return True
            
            if j - i == 1 and s[i] == s[j]:
                return True
            
            if dp[i][j] is not None:
                return dp[i][j]
            
            if s[i] != s[j]:
                return False
            
            dp[i][j] = helper(i+1, j-1)

            return dp[i][j]

        for i in range(n):
            for j in range(n):
                if helper(i,j):
                    if j - i + 1 > l:
                        l = j - i + 1
                        ans = s[i:j+1]
        return ans



