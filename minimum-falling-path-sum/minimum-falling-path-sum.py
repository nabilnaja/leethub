class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        memo = [[0] * n for _ in range(m)]
        memo[m-1] = matrix[m-1][:]
        
        for i in range (m - 2, -1,-1):
            for j in range (n):
                if j == 0:
                    min_sum = min(memo[i + 1][j], memo[i + 1][j+1]) 
                elif j == n - 1:
                    min_sum = min(memo[i + 1][j - 1], memo[i + 1][j]) 
                else:
                    min_sum = min(memo[i + 1][j - 1],memo[i + 1][j], memo[i + 1][j+1]) 
                memo[i][j] = min_sum + matrix[i][j]
                    
        return min(memo[0])
        
        