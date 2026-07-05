class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    is_bordered = self.is_bordered(board, i, j)
                    if not is_bordered:
                        self.capture(board, i, j)
    
    def is_bordered(self, board, i, j):
        if i == -1 or i == len(board):
            return True
        
        if j == -1 or j == len(board[0]):
            return True
        
        if board[i][j] == '.':
            return False
        
        if board[i][j] == 'X':
            return False
        
        old = board[i][j]
        board[i][j] = '.'
        ans = (
            self.is_bordered(board, i+1, j)
            or self.is_bordered(board, i-1, j)
            or self.is_bordered(board, i, j+1)
            or self.is_bordered(board, i, j-1)
        )
        board[i][j] = old
        return ans
    
    def capture(self, board, i, j):
        if i == -1 or i == len(board):
            return
        
        if j == -1 or j == len(board[0]):
            return
        
        if board[i][j] == 'X':
            return

        board[i][j] = 'X'

        self.capture(board, i+1, j)
        self.capture(board, i-1, j)
        self.capture(board, i, j+1)
        self.capture(board, i, j-1)


