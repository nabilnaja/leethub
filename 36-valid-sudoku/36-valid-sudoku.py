class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Time complexity: O(n**2) n is equal to 9.  
        Space complexity:  O(n**2) n is uequal to 9, we could say that we use constant space too
        """
        n = 9
        rows = [[0] * n for _ in range(n)]
        cols = [[0] * n for _ in range(n)]
        boxes = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                item = int(board[i][j]) - 1
                if rows[i][item] == 1:
                    return False
                rows[i][item] = 1
                if cols[j][item] == 1:
                    return False
                cols[j][item] = 1
                boxes_id = (i // 3) * 3 + j // 3
                if boxes[boxes_id][item] == 1:
                    return False
                boxes[boxes_id][item] = 1
        return True
                
        