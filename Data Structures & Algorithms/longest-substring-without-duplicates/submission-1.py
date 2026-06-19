class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = -1
        ans = 0
        visited = set()

        for idx, c in enumerate(s):
            if c not in visited:
                visited.add(c)
                continue
            ans = max(ans, len(visited))
            while True:
                st += 1
                if s[st] == c:
                    break
                else:
                    visited.remove(s[st])
        return max(ans, len(visited))
                
