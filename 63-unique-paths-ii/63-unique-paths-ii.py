class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        @cache
        def dp(i = 0,j = 0):
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            
            
            return dp(i, j+1) + dp(i+1, j)
        
        def dp():
            memo = [[0] * n for _ in range(m)]
              
            memo[m-1][n-1] = 0 if obstacleGrid[m-1][n-1] else 1
            
            for i in range(n-2, -1,-1):
                memo[m-1][i] = 0 if obstacleGrid[m-1][i] or not memo[m-1][i+1]  else 1 
            for j in range(m-2, -1,-1):
                memo[j][n-1] = 0 if obstacleGrid[j][n-1] or not memo[j+1][n-1] else 1 

            for i in range(m - 2, -1, -1):
                for j in range(n - 2, -1, -1):
                    if obstacleGrid[i][j] == 1 :
                        memo[i][j] = 0
                    else:
                        memo[i][j] = memo[i + 1][j] + memo[i][j + 1]

            return memo[0][0]
        return dp()
        