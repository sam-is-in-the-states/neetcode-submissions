class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = set()
        ans = 0
        st = 0

        for i, c in enumerate(s):
            if c not in m:
                m.add(c)
                ans = max(ans,(len(m)))
                continue

            while s[st] != c:
                m.remove(s[st])
                st += 1
            
            st += 1


        return ans 
