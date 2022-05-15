class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])

        @cache
        def dp(i = 0, j = 0):
            if i == m - 1 and j == n - 1 :
                return grid[i][j]
            
            if i>=m or j>=n :
                return float('inf')
            
            return min(dp(i+1,j), dp(i, j+ 1)) + grid[i][j]
        
        def dp():
            
            memo = [[0] * (n) for _ in range(m)]
            memo[m-1][n-1] = grid[m-1][n-1] 
            
            for j in range(n - 2, - 1, -1):
                memo[m-1][j] = grid[m-1][j] + memo[m-1][j + 1]
                
            for i in range(m - 2, -1 , -1):
                memo[i][n-1] = grid[i][n-1] + memo[i + 1][n-1]

            for i in range (m - 2, -1, -1):
                for j in range (n - 2, -1, -1):
                    memo[i][j] = min(memo[i+1][j], memo[i][j+ 1]) + grid[i][j]

            return memo[0][0]
        return dp()