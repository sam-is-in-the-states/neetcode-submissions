class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    self.update_island(grid, i, j)
        return islands
    
    def update_island(self, grid, i, j):
        if i == -1 or i == len(grid):
            return
        
        if j == -1 or j == len(grid[0]):
            return

        if grid[i][j] == "0":
            return

        grid[i][j] = "0"
        self.update_island(grid, i+1, j) 
        self.update_island(grid, i-1, j) 
        self.update_island(grid, i, j+1) 
        self.update_island(grid, i, j-1)