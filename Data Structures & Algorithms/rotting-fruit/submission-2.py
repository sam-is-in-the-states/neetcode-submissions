class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh_cnt = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                val = grid[i][j]
                if val == 1:
                    fresh_cnt += 1
                elif val == 2:
                    deque.append(q, (i,j))
        minutes = 0
        deque.append(q, (-1,-1))
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            x,y = deque.popleft(q)
            if x == y == -1:
                if fresh_cnt == 0:
                    return minutes
                minutes += 1
                if q:
                    deque.append(q, (-1,-1))
                continue

            if grid[x][y] == 1:
                grid[x][y] = 2
                fresh_cnt -= 1

            for dir_x, dir_y in directions:
                new_x = x + dir_x
                new_y = y + dir_y

                if new_x == -1 or new_x == len(grid):
                    continue
                if new_y == -1 or new_y == len(grid[0]):
                    continue
                
                if grid[new_x][new_y] == 1:
                    deque.append(q, (new_x, new_y))
        
        return -1
            

                