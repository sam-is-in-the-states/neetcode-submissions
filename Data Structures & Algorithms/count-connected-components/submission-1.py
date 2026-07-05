class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = set()
        visited = set()

        neighbours = {}

        for edge in edges:
            v1,v2 = edge
            nodes.add(v1)
            nodes.add(v2)
            
            if v1 in neighbours:
                neighbours[v1].append(v2)
            else:
                neighbours[v1] = [v2]
            if v2 in neighbours:
                neighbours[v2].append(v1)
            else:
                neighbours[v2] = [v1]
        
        ans = n - len(neighbours.keys())

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for n in neighbours[node]:
                dfs(n)


        for n in nodes:
            if n in visited:
                continue
            ans += 1
            dfs(n)
        
        return ans
        
            