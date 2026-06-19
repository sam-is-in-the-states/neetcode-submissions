class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set()

        m = {}
        longest = 0

        for n in nums:
            if n in visited:
                continue
            visited.add(n)
        
            st = n
            end = n

            if n-1 in m:
                st = m[n-1][0]
                m.pop(n-1)
                m.pop(st, None)
            
            if n+1 in m:
                end = m[n+1][1]
                m.pop(n+1)
                m.pop(end, None)
            
            m[st] = (st, end)
            m[end] = (st, end)

            longest = max(longest, end - st + 1)
        return longest
