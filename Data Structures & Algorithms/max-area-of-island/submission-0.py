class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(self.update_island(grid, i, j), ans)
        return ans
    
    def update_island(self, grid, i, j) -> int:
        if i == -1 or i == len(grid):
            return 0
        
        if j == -1 or j == len(grid[0]):
            return 0

        if grid[i][j] == 0:
            return 0

        grid[i][j] = 0
        ans = 1
        ans += self.update_island(grid, i+1, j) 
        ans += self.update_island(grid, i-1, j) 
        ans += self.update_island(grid, i, j+1) 
        ans += self.update_island(grid, i, j-1)

        return ans