class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = {}

        def helper(i, j):
            if j == n:
                return m-i
            if i == m:
                return n-j
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            ans = float('inf')

            # insert
            ans = min(ans, 1 + helper(i, j + 1))

            # replace
            if word1[i] == word2[j]:
                ans = min(ans, helper(i+1, j+1))
            else:
                ans = min(ans, 1 + helper(i+1, j+1))
            
            # delete
            ans = min(ans, 1 + helper(i+1, j))

            dp[(i,j)] = ans
            return ans
        
        return helper(0,0)

