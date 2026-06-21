class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u = 0
        d = len(matrix) - 1
        row = -1
        while u <= d:
            mid = (u + d) // 2
            print(u)
            print(d)
            print(mid)
            print('----')
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                row = mid
                break
            
            if target > matrix[mid][-1]:
                u = mid + 1
            else:
                d = mid - 1 

        
        if row == -1:
            return False
        
        l = 0
        r = len(matrix[0])

        while l <= r:
            mid = (l + r) // 2
            if target == matrix[row][mid]:
                return True
            
            if target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return False