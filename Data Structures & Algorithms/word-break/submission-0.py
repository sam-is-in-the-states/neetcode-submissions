class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def helper(st_idx, curr_idx, s, wordDict) -> bool:
            if st_idx == curr_idx:
                if st_idx in memo:
                    return memo[st_idx]
                else:
                    memo[st_idx] = helper(st_idx, curr_idx + 1, s, wordDict)
                    return memo[st_idx]

            if curr_idx > len(s):
                return False
            
            for word in wordDict:
                if s[st_idx:curr_idx] == word:
                    if curr_idx == len(s):
                        return True
                    ans = helper(curr_idx, curr_idx, s, wordDict)
                    if ans:
                        return True
            
            return helper(st_idx, curr_idx+1, s, wordDict)
        
        return helper(0,0,s,wordDict)
            

