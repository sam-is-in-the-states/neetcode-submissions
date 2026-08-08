class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = 1
        ans = s[0]
        n = len(s)
        for i in range(n):
            j = i - 1
            k = i + 1

            while j >= 0 and k < n:
                if s[j] != s[k]:
                    break
                j -= 1
                k += 1
            
            if k - j - 1 > l:
                l = k - j - 1
                ans = s[j+1:k]
            
            j = i
            k = i + 1

            if k == n or s[j] != s[k]:
                continue
            
            while j >= 0 and k < n:
                if s[j] != s[k]:
                    break
                j -= 1
                k += 1

            if k - j - 1 > l:
                l = k - j - 1
                ans = s[j+1:k]
        return ans

