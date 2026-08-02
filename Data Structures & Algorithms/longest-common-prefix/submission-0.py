class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        idx = 0
        if not strs:
            return ""
        while True:
            if len(strs[0]) == idx:
                return ans 
            c = strs[0][idx]
            for s in strs:
                if len(s) == idx:
                    return ans
                
                if s[idx] != c:
                    return ans
            idx += 1
            ans += c
        return ans