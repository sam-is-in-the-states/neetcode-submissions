class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def helper(board, idx_x, idx_y, idx_word):
            if idx_word == len(word):
                return True
            
            if idx_x == len(board) or idx_x < 0:
                return False
            
            if idx_y == len(board[0]) or idx_y < 0:
                return False
            
            if board[idx_x][idx_y] == '.':
                return False

            if board[idx_x][idx_y] != word[idx_word]:
                return False
            
            old = board[idx_x][idx_y]
            board[idx_x][idx_y] = '.'

            ans = (
                helper(board, idx_x+1, idx_y, idx_word+1)
                or helper(board, idx_x-1, idx_y, idx_word+1)
                or helper(board, idx_x, idx_y+1, idx_word+1)
                or helper(board, idx_x, idx_y-1, idx_word+1)
            )

            board[idx_x][idx_y] = old
            return ans
        for i in range(len(board)):
            for j in range(len(board[0])):
                ans = helper(board, i, j, 0)
                if ans:
                    return ans
        return False
