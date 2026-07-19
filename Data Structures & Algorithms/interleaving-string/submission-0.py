class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n3 != n1 + n2:
            return False
        
        m = {}

        def helper(i,j,k) -> bool:
            if k == n3:
                return True
            
            if i == n1 and j == n2:
                return False
            if (i,j) in m:
                return m[(i,j)]
            ans = False
            
            if i < n1 and s3[k] == s1[i]:
                ans = ans or helper(i+1,j,k+1)

            if j < n2 and s3[k] == s2[j]:
                ans = ans or helper(i,j+1,k+1)

            m[(i,j)] = ans 
            return ans
        
        return helper(0,0,0)