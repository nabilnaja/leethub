class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Time complexity: O(log n * m)  
        Space complexity:  O(1)        
        """
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = l + (r - l) //2
            row, col = mid // n, mid % n
            if matrix[row][col] == target:
                return True
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                l = mid + 1
        return False
        
            
        
                
        