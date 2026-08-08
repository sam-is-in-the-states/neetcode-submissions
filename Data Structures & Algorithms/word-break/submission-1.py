class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [None] * n

        def helper(idx):
            if idx == n:
                return True
            
            if dp[idx] is not None:
                return dp[idx]

            for word in wordDict:
                if idx + len(word) > n:
                    continue
                if s[idx: idx + len(word)] == word:
                    curr = helper(idx + len(word))
                    if curr:
                        dp[idx] = True
                        return True
            dp[idx] = False
            return False
        
        return helper(0)

            

