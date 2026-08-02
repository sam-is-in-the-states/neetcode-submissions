class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        ans = 0

        def helper(i):
            if i in visited:
                return
            visited.add(i)
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    helper(j)


        for i in range(len(isConnected)):
            if i in visited:
                continue
            ans += 1
            helper(i)
        
        return ans